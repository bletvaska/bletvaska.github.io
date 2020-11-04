import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def view_dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "title": "Magic Dashboard!", "temperature": 99, "timestamp": "1.1.1970 00:00:00"}
    )

if __name__ == "__main__":
    uvicorn.run('dashboard:app', host="0.0.0.0", port=5000, reload=True)
