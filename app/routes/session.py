import json
from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import current_user
from ..models import User, RecommendationHistory

router=APIRouter()
@router.get("/session-info")
def info(user:User=Depends(current_user)): return {"logged_in":True,"user_id":user.id,"name":user.name,"email":user.email}

@router.get("/session-data")
def data(user:User=Depends(current_user),db:Session=Depends(get_db)):
    rows=db.scalars(select(RecommendationHistory).where(RecommendationHistory.user_id==user.id).order_by(RecommendationHistory.created_at.desc()).limit(5)).all()
    count=db.scalar(select(func.count()).select_from(RecommendationHistory).where(RecommendationHistory.user_id==user.id))
    return {"user":{"id":user.id,"name":user.name,"email":user.email},"recommendation_count":count or 0,
            "recent":[{"id":x.id,"planner_type":x.planner_type,"budget":x.budget,"created_at":x.created_at.isoformat(),"result":json.loads(x.response_json)} for x in rows]}
