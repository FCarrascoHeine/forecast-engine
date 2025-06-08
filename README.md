# Forecast Engine

**Status:** Under Construction 🚧

Our vision for the Forecast Engine is an easy-to-use tool for generating demand forecasts from user-provided data. The goal is to provide a simple interface for computing accurate demand predictions, making it accessible for users without deep statistical or programming knowledge.

This project will start with basic features and gradually expand to include more advanced functionality and customization options.

Stay tuned for updates as new features are added!

## 🚀 Current features

- Dropdown to select a CSV file from the `data/` directory
- Confirmation page showing the selected file
- Clean, object-oriented structure ready for extension
- Serves a `favicon.ico` from `static/`
- FastAPI backend with Jinja2 templates

## ⚙️ Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**

   ```bash
   uvicorn src.main:app --reload
   ```

3. **Visit**  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📅 Roadmap Ideas

- CSV upload from browser
- Plotly Dash integration
- Database connectivity
- API endpoints for data processing
