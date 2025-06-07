from fastapi import FastAPI
from src.app.api import router  # Import your API router

app = FastAPI()

# Include the router under the root path
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # Run the app with reload for development convenience
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=False)
