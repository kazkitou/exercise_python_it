import zmq
from datetime import datetime
from time import sleep

host = "127.0.0.1"
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://{}:{}".format(host, port))
print("Client started at", datetime.utcnow())
while True:
    sleep(5)
    request = b"time"
    client.send(request)
    reply = client.recv()
    print("Client recieved {}".format(reply))
