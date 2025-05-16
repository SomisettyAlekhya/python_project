import socket
import threading
from poem import Poem
from parser import build_xml  # Use custom XML builder

class MyThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        try:
            word = self.client.recv(100).decode("utf-8").strip()
            poem = Poem("poem.txt")

            # Execute all methods 
            poem.show()
            poem.clean()
            poem.clean_1()
            poem.clean_2()

            matched_lines = poem.getLines(word)

            # Use parser.py to build XML
            xml_bytes = build_xml(word, matched_lines)

            self.client.send(xml_bytes)

        except Exception as e:
            self.client.send(f"<error>{str(e)}</error>".encode("utf-8"))

# Server setup
host = "127.0.0.1"
port = 5656
s1 = socket.socket()
s1.bind((host, port))
s1.listen()

print("Server is listening...")

while True:
    client, addr = s1.accept()
    print(f"Connected with {addr}")
    t1 = MyThread(client)
    t1.start()