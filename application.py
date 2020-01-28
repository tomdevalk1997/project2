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
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# messages = [[channel, timestamp, message, user], [channel, timestamp, message, user]]
messages = []
channels = []
users = []

@app.route("/")
def index():
    display_name = "Tom"
    status = "Active"
    channel_title = "Channel 1"
    channels = ["Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5", "Channel 6", "Channel 7", "Channel 8", "Channel 9", "Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14", "Channel 15", "Channel 16"]
    return render_template("index.html", display_name=display_name, status=status, channel_title=channel_title, channels=channels)

@socketio.on("send message")
def send_message(data):
    selection = data["selection"]

    channel = data["channel"]
    timestamp = datetime.datetime()
    message = data["message"]
    user = data["user"]

    messages.append([channel, timestamp, message, user])
    emit("message sent", messsages, broadcast=True)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

def search(data):
    pass

def new_channel(data):
    channels.append(f"{new_channel_name}")
