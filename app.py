import requests
import json
from flask import Flask, request, render_template, session, url_for, jsonify
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = 'my-secret-key'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['WTF_CSRF_CHECK_DEFAULT'] = False

url = "https://seal-app-aafp5.ondigitalocean.app/query"
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsIkZ1bGxOYW1lIjoiS290dGlsdWtrYWwgQXJ1biBLZXNhdmFuIiwiQ29udHJhY3RFbWFpbCI6Ind3dy5sb2NhbGhvc3Q4MDg2LmNvbUBnbWFpbC5jb20iLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.uHSJPxwGWOfCPyQ8Y0cBw7UF2VfWYv3KrHDl-adlPFA',
    'Content-Type': 'application/json'
}

# csrf = CSRFProtect(app)

@app.route("/")
# @csrf.exempt
def home():
    return render_template("index.html")

@app.post("/searchResult")
def searchResult():
    query = request.form['query']

    payload = json.dumps({
    "queries": [
        {
            "query": query
        }
    ]
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data = json.loads(response.text)

    context = {
        "query": query,
        "results":data["results"][0]["results"]
    }


    return render_template("search_results.html", context=context)
