from flask import Flask
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, cors_allowed_origins="*")
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

CORS(app)

@socketio.on('itemAdded')
def handleMessage(msg):
    print(msg)
    socketio.emit('itemAdded', msg)
    #send(msg, broadcast=True)

@socketio.on('itemUpdated')
def handleMessage(msg):
    print(msg)
    socketio.emit('itemUpdated', msg)
    #send(msg, broadcast=True)

@socketio.on('itemDeleted')
def handleMessage(msg):
    print(msg)
    socketio.emit('itemDeleted', msg)
    #send(msg, broadcast=True)


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('connection_status', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


from views import *

if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)