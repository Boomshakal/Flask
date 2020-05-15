import json
from flask import Flask, request
from geventwebsocket.websocket import WebSocket
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

app_ws = Flask(__name__)

@app_ws.route("/ws")
def ws():
    user_socket=request.environ.get("wsgi.websocket")	# type:WebSocket
    while 1:
        msg = user_socket.receive()
        user_socket.send(msg)

if __name__ == '__main__':
    http_server= WSGIServer(("0.0.0.0",9527),app_ws,handler_class=WebSocketHandler)
    http_server.serve_forever()