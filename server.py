import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Er Is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
