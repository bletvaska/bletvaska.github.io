from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get('/hello')
def hello_with_template():
    tpl = templates.TemplateResponse('hello.html', {})
    print(tpl)
    pass
