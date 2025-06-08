from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.services.data_loader import DataLoader

# Create an APIRouter instance to group routes related to file selection
router = APIRouter()

# Setup Jinja2 template rendering pointing to the templates directory
templates = Jinja2Templates(directory="src/templates")

# Initialize the data loader service to list CSV files
data_loader = DataLoader()

@router.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    """
    Handle GET requests to '/'.
    List all CSV files available in the data folder and
    render the file selection page.
    """
    files = data_loader.list_csv_files()
    # Render select.html passing the request context and available files
    return templates.TemplateResponse("select.html", {"request": request, "files": files})

@router.post("/select", response_class=HTMLResponse)
async def handle_selection(request: Request, selected_file: str = Form(...)):
    """
    Handle POST requests to '/select'.
    Accept the selected file name from the form submission,
    and render the selection page again with a confirmation message.
    """
    # Load the selected CSV file as a DataFrame
    df = data_loader.load_csv_as_df(selected_file)
    entry_count = len(df)

    return templates.TemplateResponse("select.html", {
        "request": request,
        "selected_file": selected_file,           # The filename chosen by user
        "entry_count": entry_count,               # Number of entries in the selected file
        "files": data_loader.list_csv_files(),    # Re-fetch files to populate dropdown
        "confirmation": True                      # Flag to show confirmation message
    })
