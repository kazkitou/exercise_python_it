''' plint test. '''
import string
import zmq

HOST = '127.0.0.1'
PORT = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://{}:{}'.format(HOST, PORT))

with open('mammoth.txt', 'rt') as poem:
    words = poem.read()
for word in words.split():
    word = word.strip(string.punctuation)
    data = word.encode('utf-8')
    if word.startswith(('a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O')):
        pub.send_multipart([b'vowels', data])
    if len(word) == 5:
        pub.send_multipart([b'five', data])
