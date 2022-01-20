import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    sio.send(f"\nClient {sio.sid} connected...\n")

@sio.on('custom event')
def receive_custom(msg):
    print(msg)

sio.connect('52.196.51.209:8082')
# sio.wait() # cannot keyboard interrupt this
sio.sleep(10)
sio.disconnect()