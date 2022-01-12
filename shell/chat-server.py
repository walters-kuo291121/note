# -*- coding: UTF-8 -*-
import os
from flask import Flask, render_template
from flask_socketio import SocketIO,emit,join_room,leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*')

@socketio.on('chat', namespace='/chat')  
def handle_message(data): 
    username = data['username']
    room = data['roomId'] 
    message = data['message']
    emit('response', {'userName':username,'message':message},broadcast=True,room=room)
  
@socketio.on('connect', namespace='/chat')  
def test_connect(): 
     print('Client connected') 
#    emit('response', {'data': 'Connected'})  

@socketio.on('disconnect', namespace='/chat')  
def test_disconnect():  
    print('Client disconnected') 

@socketio.on('join', namespace='/chat')
def on_join(data):
    print(data)
    username = data['username']
    room = data['roomId']
    join_room(room)
    if username:
        msg=username+'加入直播間'+str(room)
        emit('join-msg', {'data': msg},broadcast=True,room=room)  

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['roomId']
    leave_room(room)
    if username:
        msg=username + '離開直播間'+str(room)
        emit('join-msg', {'data': msg}, broadcast=True,room=room)  

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=int(os.environ.get("PORT", 8080)),debug=True)