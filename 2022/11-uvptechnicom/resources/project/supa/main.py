from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s: %(message)s')
logger = logging.getLogger('supa')

# fastapi app init
app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent / 'static'), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent / 'templates')


# homepage endpoint
@app.get('/')
def homepage(request: Request):
    logger.info(f'Incomming client from {request.client.host}')
    return templates.TemplateResponse("homepage.html", {'request': request})


@app.get('/deadlock')
def deadlock():
    logger.info('Ta tu si sa dostal')

    while True:
        pass

    logger.info('ta ale odtialto sa uz nedostanes')


@app.get('/health')
def check_health():
    return {
        'status': 'up'
    }


# main entrypoint
def main():
    logger.info('Starting Application')
    uvicorn.run('supa.main:app', reload=True, host='0.0.0.0')
    #, log_level="critical")


if __name__ == '__main__':
    main()
