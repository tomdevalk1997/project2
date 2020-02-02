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
from datetime import datetime
from flask_socketio import SocketIO, emit, join_room, leave_room

# to avoid errors in python application.py
from gevent import monkey as curious_george
curious_george.patch_all(thread=False, select=False)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channel_list = {"general": [] }
present_channel = {"initial":"general"}

@app.route("/")
def index():
    logged_in = True
    if logged_in:
        display_name = "Tom"
        status = "Active"
        channel_title = "Channel 1"
        channels = ["Channel 1", "Channel 2", "Channel 3", "Channel 4", "Channel 5", "Channel 6", "Channel 7", "Channel 8", "Channel 9", "Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14", "Channel 15", "Channel 16"]
    else:
        display_name = ""
        status = ""
        channel_title = ""
        channels = []
    return render_template("index.html", display_name=display_name, status=status, channel_title=channel_title, channels=channels, logged_in=logged_in)

@socketio.on('new_connection')
def new_connection(data):
    print(data["message_connection"])

@socketio.on('test_message')
def test_message(data):
    print(data["message"])

@socketio.on('send_message')
def send_message(data):
    message = data['message']
    timestamp = datetime.now()
    timestamp_string = timestamp.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{message} sent at {timestamp_string}")

    #messages.append([message, timestamp])
    #emit("message_sent", {"messages": messages}, broadcast=True)

@socketio.on('joinroom')
def joinroom():
    username = "Tom"
    room = 1
    join_room(room)
    print(f"Entered room {room}")
    send(username + ' has entered the room.', room=room)

@socketio.on('connectToRoom')
def connectToRoom(data):
    print(data)

@socketio.on('leaveroom')
def leaveroom():
    username = "Tom"
    room = 1
    leave_room(room)
    print(f"Left room {room}")
    send(username + ' has entered the room.', room=room)

@socketio.on('search')
def search(data):
    pass

@socketio.on('new_channel')
def new_channel(data):
    pass

if __name__ == '__main__':
    socketio.run(app, debug=True)
