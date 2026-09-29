import json
from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import current_user
from ..models import User, RecommendationHistory
from ..services.recommendation_service import generate

router=APIRouter()

def save(db,user,planner,budget,payload,result):
    db.add(RecommendationHistory(user_id=user.id,planner_type=planner,budget=budget,
        request_json=json.dumps(payload),response_json=json.dumps(result))); db.commit()

def check_budget(b):
    if b<100 or b>10_000_000: raise HTTPException(422,"Budget must be between ₹100 and ₹1 crore")

@router.post("/generate-home")
def home(budget:int=Form(...),rooms:str=Form("Living Room"),style:str=Form("Modern"),notes:str=Form(""),
         user:User=Depends(current_user),db:Session=Depends(get_db)):
    check_budget(budget); p={"budget":budget,"rooms":[x.strip() for x in rooms.split(",") if x.strip()],"style":style,"notes":notes}
    r=generate("home",p); save(db,user,"home",budget,p,r); return r

@router.post("/generate-party")
def party(budget:int=Form(...),guests:int=Form(...),event_type:str=Form("Birthday"),venue:str=Form("Home"),notes:str=Form(""),
          user:User=Depends(current_user),db:Session=Depends(get_db)):
    check_budget(budget)
    if not 1<=guests<=5000: raise HTTPException(422,"Guests must be between 1 and 5000")
    p={"budget":budget,"guests":guests,"event_type":event_type,"venue":venue,"notes":notes}
    r=generate("party",p); save(db,user,"party",budget,p,r); return r

@router.post("/generate-jewelry")
async def jewelry(budget:int=Form(...),occasion:str=Form("Casual"),style:str=Form("Minimal"),metal:str=Form("Any"),notes:str=Form(""),
                  outfit_image:UploadFile|None=File(None),user:User=Depends(current_user),db:Session=Depends(get_db)):
    check_budget(budget); raw=None; mime=None
    if outfit_image and outfit_image.filename:
        if outfit_image.content_type not in {"image/jpeg","image/png","image/webp"}: raise HTTPException(400,"Upload JPG, PNG or WEBP only")
        raw=await outfit_image.read()
        if len(raw)>5*1024*1024: raise HTTPException(413,"Image must be 5 MB or smaller")
        mime=outfit_image.content_type
    p={"budget":budget,"occasion":occasion,"style":style,"metal":metal,"notes":notes,"outfit_image_attached":bool(raw)}
    r=generate("jewelry",p,raw,mime); save(db,user,"jewelry",budget,p,r); return r

@router.get("/recommendations-details")
def details(): return {"planner_types":["home","party","jewelry"],"message":"Use the planner POST endpoints to generate recommendations."}

@router.get("/startup")
def startup(): return {"status":"ready"}
