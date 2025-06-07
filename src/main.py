from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse

import io
import os
import pandas as pd

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    """
    Home page endpoint:
    - Serves a simple HTML form for uploading a CSV file.
    - This is the main entry point for users to interact with the app.
    """
    return """
    <h1>CSV File Upload</h1>
    <p>Upload a CSV file to see its dimensions.</p>
    <form action="/upload-csv/" enctype="multipart/form-data" method="post">
        <input name="file" type="file" accept=".csv">
        <input type="submit" value="Upload">
    </form>
    """

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """
    Favicon endpoint:
    - Handles requests for the browser's favicon (the small icon in the browser tab).
    - Prevents 404 errors in logs when the browser looks for /favicon.ico.
    """
    return FileResponse(os.path.join("static", "favicon.ico"))

@app.post("/upload-csv/", response_class=HTMLResponse)
async def upload_csv(file: UploadFile = File(...)):
    """
    CSV upload endpoint:
    - Handles POST requests from the upload form.
    - Accepts a CSV file, reads it into a pandas DataFrame, and returns the number of rows and columns.
    - If the file is not a CSV or an error occurs, returns an error message.
    """
    if not file.filename.endswith('.csv'):
        return HTMLResponse(content="<h2>Error: Only CSV files are allowed.</h2>", status_code=400)

    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        df = pd.read_csv(io.StringIO(decoded))
        row_count, col_count = df.shape
    except Exception as e:
        return HTMLResponse(content=f"<h2>Error: {e}</h2>", status_code=500)

    return f"""
    <h1>Upload Result</h1>
    <p><strong>Filename:</strong> {file.filename}</p>
    <p><strong>Rows:</strong> {row_count}</p>
    <p><strong>Columns:</strong> {col_count}</p>
    <a href="/">Upload another file</a>
    """

# To run this app, use the following command in your terminal:
# uvicorn src.main:app --reload
# Then open your browser at http://127.0.0.1:8000/
