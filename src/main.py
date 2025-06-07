from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Under construction</h1>"

# To run this app, use the following command in your terminal:
# uvicorn src.main:app --reload
# Then open your browser at http://127.0.0.1:8000/