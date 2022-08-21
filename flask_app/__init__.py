from flask import Flask 
import re
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.secret_key = "this_is_secret"
bcrypt = Bcrypt( app )

DATABASE = "Bear_sightings_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 