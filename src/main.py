from fastapi import FastAPI
from src.routes.csv_routes import router as csv_router

app = FastAPI()

app.include_router(csv_router)

# To run this app, use the following command in your terminal:
# uvicorn src.main:app --reload
# Then open your browser at http://127.0.0.1:8000/
