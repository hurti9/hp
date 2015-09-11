from flask import render_template, jsonify, request
from app import app
from wtforms.validators import DataRequired, NumberRange, Regexp, Optional
from wtforms import TextField, IntegerField, Form, TextAreaField, HiddenField
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
@app.route('/')
def front():
    return render_template("front.html")
