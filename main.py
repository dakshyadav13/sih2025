from fileinput import filename
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash

import otp_email
from otp_email import finding_current_otp, writing_otp

app = Flask(__name__)

@app.route("/")
def to_page():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
