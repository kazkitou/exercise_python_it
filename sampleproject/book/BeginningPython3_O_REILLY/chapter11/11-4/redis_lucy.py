import redis
from datetime import datetime
from time import sleep

conn = redis.Redis(host="localhost", port=6789)
timeout = 10
conveyor = "chocolates"
while True:
    sleep(0.5)
    msg = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if msg:
        piece = msg[1]
        print("Lucy got a", piece, "at", datetime.utcnow(), ", only", remaining, "left")
