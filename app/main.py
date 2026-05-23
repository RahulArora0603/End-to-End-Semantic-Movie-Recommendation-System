'''
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.recommender import recommend

app = FastAPI()

# static folder
app.mount('/static', StaticFiles(directory='app/static'), name='static')

# templates
templates = Jinja2Templates(directory='app/templates')


# homepage
@app.get('/')
def home(request: Request):

    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'recommendations': []
        }
    )


# recommendation route
@app.post('/recommend')
def get_recommendations(
    request: Request,
    movie_name: str = Form(...)
):

    recommendations = recommend(movie_name)

    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'recommendations': recommendations,
            'movie_name': movie_name
        }
    )
    '''

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.recommender import recommend

app = FastAPI()

# static folder
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# templates
templates = Jinja2Templates(
    directory="app/templates"
)


# homepage
@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "recommendations": []
        }
    )


# recommendation route
@app.post("/recommend")
def get_recommendations(
    request: Request,
    movie_name: str = Form(...)
):

    recommendations = recommend(movie_name)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "recommendations": recommendations,
            "movie_name": movie_name
        }
    )