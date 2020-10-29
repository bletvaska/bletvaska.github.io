from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from jinja2 import Template
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def hello():
    return {
            "name": "jano",
            "surname": "hrasko"
            }

@app.get('/hello/{name}')
def hello_johnny(name: str):
    return {
                'meno': name
            }


@app.get('/test/{number}')
def numeric_test(number: int):
    return {
                'number': number
            }


@app.get('/html/{name}')
def html_hello(name: str):
    template = Template('<h1>{{ name }} je makac</h1>')

    return HTMLResponse(template.render({'name': name})) 


@app.get('/home')
def home(request: Request, response_class=HTMLResponse):
    payload = {
            "request": request, 
            "name": "juraj", 
            "temperature": 23.4
            }
    return templates.TemplateResponse('home.html', payload)
