from fileinput import filename
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash

import otp_email
from otp_email import finding_current_otp, writing_otp

app = Flask(__name__)

@app.route("/")
def to_page():
    return render_template("index.html")

# @app.route("/login.html", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         # Validate form data
#         password = request.form.get("password")
#         email = request.form.get("email")
#
#         if not (password and email):
#             return render_template("login.html", message="All fields are required.")
#
#         # Hash the password
#         hashed_password = generate_password_hash(password)
#
#         filename = "database.txt"
#         with open(filename, 'w') as file:
#             file.write(email)
#
#         otp_email.sending_email()
#
#         return redirect("/otp")
#
#     return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     # Validate form data
    #     password = request.form.get("passwordlogin")
    #     username = request.form.get("usernamelogin")
    #
    #     # if not (password and username):
    #     #     return render_template("login.html", message="All fields are required.")
    #
    #     # Hash the password
    #     hashed_password = generate_password_hash(password)
    #
    #     return redirect("/")

    return render_template("login.html")
#
# @app.route("/low key similutor", methods=["GET", "POST"])
# def low_key_simulator():
#     return render_template("low_key_similutor.html")
#
# @app.route("/otp", methods=["GET", "POST"])
# def otp_submittion():
#     if request.method == "POST":
#         otp = request.form.get("otp")
#
#         if not (otp):
#             return render_template("otp.html", message="All fields are required.")
#
#         if otp == finding_current_otp():
#             return redirect("/mainpage")
#
#         if otp != finding_current_otp():
#             return render_template("otp.html", message="Wrong otp")
#
#     return render_template("otp.html")
#
# @app.route("/mainpage")
# def main_page():
#     return render_template("mainpage.html")