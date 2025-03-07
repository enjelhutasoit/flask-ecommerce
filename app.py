from flask import Flask, render_template, request

app = Flask(__name__)

GENDERS = [
    "Female", 
    "Male", 
    "Prefer not to say"
]

@app.route("/")
def index():
      return render_template("index.html", genders=GENDERS)
    
@app.route("/register", methods=["POST"])
def register():
   if not request.form.get("name") or request.form.get("gender") not in GENDERS:
      return render_template("failure.html")
   return render_template("success.html")