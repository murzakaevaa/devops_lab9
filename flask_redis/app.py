from flask import Flask
import redis
import socket
import os

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return db.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World VERSION 5! I have been seen {} times. My name is: {}\n'.format(count, socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
