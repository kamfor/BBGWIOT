#!/usr/bin/env python
"""
This script runs the FlaskWebProject1 application using a development server.
"""
from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import  render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from FlaskWebProject1 import app
import sensor

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='gevent')
thread = None

def background_thread():
    """Example of how to send server generated events to clients."""
    noise = 0
    proximity = 0
   

    while True:
        time.sleep(1)
        print("Hello")
        noise = sensor.NoiseRead()
        proximity = sensor.ProxRead()

        socketio.emit('my data',
                      {'data1': proximity,'data2': noise, },
                      namespace='/test')

@socketio.on('my relay', namespace='/test')
def deal_relay(message):
    print("Recive the button info.")
    if message['data'] == "Open1":
        sensor.ControlRelay1(0)
        print("Open the relay 1")
    if message['data'] == "Close1":
        sensor.ControlRelay1(1)
        print("Close the relay 1")
    if message['data'] == "Open2":
        sensor.ControlRelay2(0)
        print("Open the relay 2")
    if message['data'] == "Close2":
        sensor.ControlRelay2(1)
        print("Close the relay 2")

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)




if __name__ == '__main__':
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()
    socketio.run(app,'0.0.0.0',8000, debug=True)
