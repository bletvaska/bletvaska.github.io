import json
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND,HTTP_303_SEE_OTHER


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def view_dashboard(request: Request):
    data = json.load(open('data.json'))
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "title": "Magic Dashboard!", "temperature": data['temperature'], "timestamp": data['timestamp']}
    )


@app.get("/form", response_class=HTMLResponse)
async def view_form(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {"request": request}
    )


@app.post("/form")
async def process_form(request: Request, temperature: float = Form(...)):
    now = datetime.now()
    data = {'temperature': str(temperature), 'timestamp': now.strftime("%d.%m.%Y %H:%M:%S")}
    with  open('data.json', 'w+') as file:
        json.dump(data, file)

    response = RedirectResponse(url='/dashboard', status_code=HTTP_303_SEE_OTHER)
    return response

if __name__ == "__main__":
    uvicorn.run('dashboard:app', host="0.0.0.0", port=5000, reload=True)
