from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={},
    )


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={},
    )


@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="profile.html",
        context={},
    )


@app.get("/games", response_class=HTMLResponse)
def games(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="games.html",
        context={},
    )


@app.get("/procurar", response_class=HTMLResponse)
def procurar(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="procurar.html",
        context={},
    )


@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )
