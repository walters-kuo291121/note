'''import socket

HOST = '52.196.51.209'
#HOST = 'http://chat.topyl666.com'
PORT = 8082
clientMessage = 'Hello!'

data = {'user_name' : 'walters', 'roomId' : 123}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.on('join', data)

client.close()'''

import socketio
sio = socketio.Client()
data = {'roomId' : 123, 'message' : 'bala'} 
   

@sio.event
def connect(namespace='/chat'):
    print('connection established')

@sio.event
def my_message(data, namespace='/chat'):
    print('message received with ', data)
    sio.emit('chat', data)
    #sio.emit('chat', {'response': 'my response'})

@sio.event
def chat(data, namespace='/chat'):
    print('chat established')
    sio.emit('chat', data)

@sio.event
def disconnect(namespace='/chat'):
    print('disconnected from server')

sio.connect('http://44.201.162.136:8080', namespaces=['/chat'])
sio.wait()

sio.chat(data)
sio.disconnect()

