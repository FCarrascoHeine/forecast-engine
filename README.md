# Forecast Engine

**Status:** Under Construction 🚧

Forecast Engine is an easy-to-use tool for generating demand forecasts from user-provided data. The goal is to provide a simple interface for uploading your data and receiving accurate demand predictions, making it accessible for users without deep statistical or programming knowledge.

This project will start with basic forecasting features and gradually expand to include more advanced functionality and customization options.

## Features (initial version)
- Upload your own demand data (CSV)
- Simple web interface

## Usage Instructions

### 1. Setup Python Virtual Environment

It is recommended to use a virtual environment to isolate dependencies.

#### Using `venv` (built-in Python module):

1. Open a terminal and navigate to the project root folder (the folder containing `src`).

2. Create a virtual environment named `.venv`:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

- On **Windows** (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- On **Windows** (CMD):

```cmd
.\.venv\Scripts\activate.bat
```

- On **Linux/macOS**:

```bash
source .venv/bin/activate
```

4. Upgrade `pip` (optional but recommended):

```bash
pip install --upgrade pip
```

---

### 2. Install Required Packages

With the virtual environment activated, install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application Locally

To start the FastAPI web server and access the app on your local machine:

1. Make sure you are in the project root folder (containing `src`).

2. Run the app using:

```bash
python -m src.main
```

3. Open your web browser and go to:

```
http://127.0.0.1:8000
```

You should see the upload page where you can select and upload a CSV file.

### Notes

- To stop the server, press `Ctrl + C` in the terminal.

- Make sure to always activate the virtual environment before running the app or installing packages.



Stay tuned for updates as new features are added!
