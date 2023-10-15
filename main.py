from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as summary_wiki
from mylib.logic import phrase as phrase_wiki

app = FastAPI()


@app.get("/")
async def root():
    """Return default value"""
    default = summary_wiki()
    print(default)
    return {"message": "Welcome to the web interface!", "default": default}


@app.get("/search/{value}")
async def search(value: str):
    """Search Wikipedia for Value"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/summary/{value}")
async def summary(value: str):
    """Retreive Wikipedia Page"""
    result = summary_wiki(value)
    return {"result": result}


@app.get("/phrases/{value}")
async def phrases(value: str):
    """Retreive Wikipedia Page"""
    result = phrase_wiki(value)
    return {"result": result}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
