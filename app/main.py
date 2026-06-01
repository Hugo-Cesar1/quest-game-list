from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


def render_page(request: Request, template_name: str) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name=template_name,
        context={},
    )

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return render_page(request, "login.html")


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return render_page(request, "register.html")


@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request):
    return render_page(request, "profile.html")


@app.get("/games", response_class=HTMLResponse)
def games(request: Request):
    return render_page(request, "games.html")


@app.get("/procurar", response_class=HTMLResponse)
def procurar(request: Request):
    return render_page(request, "procurar.html")


@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return RedirectResponse(url="/", status_code=307)
