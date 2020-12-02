#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect,send

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecret'
socketio = SocketIO(app)

@socketio.on("message")
def handleMessage(msg):
	print('Message'+msg)
	send(msg,broadcast=True)

@app.route("/")
def fun():
	return "hello would "

if __name__ == '__main__':
    socketio.run(app,debug=True)
    
    
    
    
    