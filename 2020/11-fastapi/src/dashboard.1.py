import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def view_dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "title": "Magic Dashboard!",
            "temperature": 12.34,
            "timestamp": '11.11.2020 14:30:00'
        }
    )

if __name__ == "__main__":
    uvicorn.run('dashboard:app',
                host="0.0.0.0",
                port=5000,  # default port is 8000
                reload=True)
