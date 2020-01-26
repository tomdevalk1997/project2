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
#from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#socketio = SocketIO(app)

# messages = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():
    display_name = "Tom"
    status = "Active"
    members = ["Tom", "Rebecca"]
    channel_title = "Channel 1"
    channels = ["Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5", "Channel 6", "Channel 7", "Channel 8", "Channel 9", "Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14", "Channel 15", "Channel 16"]
    return render_template("index.html", display_name=display_name, status=status, channel_title=channel_title, channels=channels, members=members)

# @socketio.on("send message")
# def send_message(data):
#     selection = data["selection"]
#     votes[selection] += 1
#     emit("vote totals", votes, broadcast=True)
