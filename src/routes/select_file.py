from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..services.data_loader import DataLoader

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")
data_loader = DataLoader()

@router.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    files = data_loader.list_csv_files()
    return templates.TemplateResponse("select.html", {"request": request, "files": files})

@router.post("/select", response_class=HTMLResponse)
async def handle_selection(request: Request, selected_file: str = Form(...)):
    return templates.TemplateResponse("select.html", {
        "request": request,
        "selected_file": selected_file,
        "files": data_loader.list_csv_files(),
        "confirmation": True
    })
