import os
from flask import Flask, session
from flask import url_for
from flask import render_template
from flask import redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import request
import requests
import json
import datetime
#from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#socketio = SocketIO(app)

@app.route("/")
def index():
    display_name = "Tom"
    status = "Active"
    members = ["Tom", "Rebecca"]
    channel_title = "Channel 1"
    channels = ["Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5", "Channel 6", "Channel 7", "Channel 8"]
    return render_template("index.html", display_name=display_name, status=status, channel_title=channel_title, channels=channels, members=members)
