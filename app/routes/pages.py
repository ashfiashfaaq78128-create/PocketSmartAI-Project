from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parents[2] / "templates")
)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@router.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )


@router.get("/planner/home", response_class=HTMLResponse)
def home_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={}
    )


@router.get("/planner/party", response_class=HTMLResponse)
def party_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={}
    )


@router.get("/planner/jewelry", response_class=HTMLResponse)
def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={}
    )


@router.get("/history-page", response_class=HTMLResponse)
def history_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={}
    )