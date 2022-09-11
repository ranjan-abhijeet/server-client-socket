import socket
import pickle


class Network(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.42.171.32"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):

        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except Exception as err:
            print(f"[-] Error while connecting...: {err}")

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
            
        except socket.error as err:
            print(f"[-] Error while sending data...: {err}")
