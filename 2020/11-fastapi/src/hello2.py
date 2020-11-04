#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run('hello:app', 
                host="0.0.0.0", 
                port=5000,  # default port is 8000
                reload=True)
