from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from .config import get_settings
from .database import Base, engine
from .routes import auth, history, pages, planners, session

settings=get_settings(); BASE=Path(__file__).resolve().parents[1]
@asynccontextmanager
async def lifespan(app):
    Base.metadata.create_all(bind=engine)
    yield

app=FastAPI(title=settings.app_name,version="1.0.0",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
app.add_middleware(SessionMiddleware,secret_key=settings.secret_key)
app.mount("/static",StaticFiles(directory=str(BASE/"static")),name="static")
app.include_router(pages.router)
app.include_router(auth.router,prefix="/api",tags=["auth"])
app.include_router(session.router,prefix="/api",tags=["session"])
app.include_router(history.router,prefix="/api",tags=["history"])
app.include_router(planners.router,prefix="/api",tags=["planners"])

@app.get("/health")
def health(): return {"status":"ok","app":settings.app_name}

if __name__=="__main__":
    import uvicorn; uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=True)
