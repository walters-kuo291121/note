import socketio
from flask import Flask
from flask_socketio import socketio

app = Flask(__name__)
# create a Socket.IO server
sio = socketio.Server(logger=True, engineio_logger=True)

# wrap with a WSGI application
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ')

if __name__ == '__main__':
    app.run(app)