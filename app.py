from flask import Flask, render_template, request

app = Flask(__name__)

GENDERS = [
    "Female", 
    "Male", 
    "Prefer not to say"
]

RESIGTRANTS = {}

@app.route("/")
def index():
      return render_template("index.html", genders=GENDERS)
    
@app.route("/register", methods=["POST"])
def register():
   name = request.form.get("name")
   if not name:
       return render_template("failure.html", message="You must provide a name.")
   
   gender = request.form.get("gender")
   if not gender:
       return render_template("failure.html", message="You must provide a gender.")
   
   if gender not in GENDERS:
        return render_template("failure.html", message="You must select from the available genders.")
   
   RESIGTRANTS[name] = gender

   return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=RESIGTRANTS)