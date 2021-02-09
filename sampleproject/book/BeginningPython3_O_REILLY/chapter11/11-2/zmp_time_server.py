import zmq
from datetime import datetime

host = "127.0.0.1"
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://{}:{}".format(host, port))
print("Server started at", datetime.utcnow())
while True:
    # クライアントからの次の要求を待つ
    message = server.recv()
    if message == b"time":
        now = datetime.utcnow()
        reply = str(now)
        server.send(bytes(reply, "utf-8"))
        print("Server sent", reply)
