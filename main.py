# This script creates a simple web app that displays "Under construction" in your browser.
# It uses the Flask library, which is easy to use for small web applications.
# To run this, you need to install Flask first:
#   pip install flask
#
# Then, run this script:
#   python main.py
#
# After running, open your browser and go to http://127.0.0.1:5000/

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Under construction</h1>"

if __name__ == "__main__":
    app.run(debug=True)
