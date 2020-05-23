import json
from flask import Flask, request
from geventwebsocket.websocket import WebSocket
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

app_ws = Flask(__name__)
user_dict = {}


@app_ws.route("/ws/<username>")
def ws(username):
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    user_dict[username] = user_socket
    while 1:
        msg = user_socket.receive()
        u_msg = {'from_user': username, 'chat': msg}  # 将接收的数据进行处理(处理成字典)
        for uname, usocket in user_dict.items():  # 循环发送向每个服务器进行发送数据
            usocket.send(json.dumps(u_msg))


@app_ws.route('/my_ws/<username>')
def my_ws(username):
    user_socket = request.environ.get('wsgi.websocket')
    # print(user_socket)
    user_dict[username] = user_socket
    print(user_dict)
    while True:
        msg = user_socket.receive()
        print(msg)
        msg_dict = json.loads(msg)
        msg_dict['from_user'] = username
        to_user = msg_dict.get('to_user')
        usocket = user_dict.get(to_user)
        if not usocket:
            continue
        try:
            usocket.send(json.dumps(msg_dict))
        except:
            user_dict.pop(to_user)


if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0", 9527), app_ws, handler_class=WebSocketHandler)
    http_server.serve_forever()
