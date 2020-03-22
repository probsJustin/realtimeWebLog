#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/log')
def log():
    socketio.emit('my_response',
                  {'data': request.args.get('body'), 'count': 0},
                  namespace='/test')
    return str(request.args.get('body'))


if __name__ == '__main__':
    socketio.run(app, debug=True)