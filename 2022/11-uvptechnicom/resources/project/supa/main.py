from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

import logging
logging.basicConfig(level=logging.INFO)

# fastapi app init
app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent / 'static'), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent / 'templates')


# homepage endpoint
@app.get('/')
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {'request': request})


# main entrypoint
def main():
    logging.info('Starting Application')
    uvicorn.run('supa.main:app', reload=True, host='0.0.0.0', log_level="critical")


if __name__ == '__main__':
    main()
