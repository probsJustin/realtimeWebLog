#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def line(funcString):
    try:
        return funcString + '\n'
    except Exception as error:
        return funcString

def append(funcString, funcStringApp):
    try:
        funcString = funcString + funcStringApp
        return funcString
    except Exception as error:
        return str(error)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/log')
def log():
    socketio.emit('my_response',
                  {'data': request.args.get('body'), 'count': 0},
                  namespace='/test')
    return str(request.args.get('body'))


@app.route('/apiTest_GET')
def apiTest_GET():
    returnObject = ""
    try:
        returnObject += line("USER: " + request.args.get("weblogUser"))
    except Exception as error:
        returnObject += line("USER: NO USER FOUND FOR PARAM weblogUser")

    for x in request.headers.keys():
        returnObject += line(str(x) + " : " + str(request.headers.get(x)))

    socketio.emit('my_response',
                  {'data': returnObject, 'count': 0},
                  namespace='/test')
    return returnObject


if __name__ == '__main__':
    socketio.run(app, debug=True)