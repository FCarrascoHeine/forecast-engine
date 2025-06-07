from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .core import CSVProcessor

router = APIRouter()
templates = Jinja2Templates(directory="src/app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the upload page with form.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload-csv", response_class=HTMLResponse)
async def upload_csv(request: Request, file: UploadFile = File(...)):
    """
    Handle CSV file upload, process it and return success message with details.
    """
    # Use CSVProcessor to read CSV from UploadFile's file-like object
    processor = CSVProcessor()
    try:
        df = await processor.read_csv(file)
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Failed to process file: {e}"
            }
        )

    # Prepare context data for template
    context = {
        "request": request,
        "filename": file.filename,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "success": True,
    }

    return templates.TemplateResponse("index.html", context)
