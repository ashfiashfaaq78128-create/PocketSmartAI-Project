import json
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import get_db
from ..dependencies import current_user
from ..models import User, RecommendationHistory
from ..schemas import HistoryItem

router=APIRouter()
@router.get("/history",response_model=list[HistoryItem])
def history(user:User=Depends(current_user),db:Session=Depends(get_db)):
    rows=db.scalars(select(RecommendationHistory).where(RecommendationHistory.user_id==user.id).order_by(RecommendationHistory.created_at.desc())).all()
    return [HistoryItem(id=x.id,planner_type=x.planner_type,budget=x.budget,created_at=x.created_at.isoformat(),result=json.loads(x.response_json)) for x in rows]
