from fastapi import FastAPI
from fastapi.responses import FileResponse
from src.routes import select_file

app = FastAPI()

# Include icon route to serve favicon and prevent 404 errors
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

app.include_router(select_file.router)

# To run this app, use the following command in your terminal:
# uvicorn src.main:app --reload
# Then open your browser at http://127.0.0.1:8000/
