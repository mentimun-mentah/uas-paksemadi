import socket, sys

class Client:
    _TCP_IP = '127.0.0.1'
    _TCP_PORT = 8081
    _BUFFER_SIZE = 1024
    _MESSAGE = b"Ping Pong"

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self._TCP_IP,self._TCP_PORT))
        self.client.send(self._MESSAGE)
        print("====== waiting server ======\n")

    def Request(self) -> bytes:
        data = self.client.recv(self._BUFFER_SIZE)
        # for file transfer TCP Client
        self.save_data(data)
        if not data:
            print('\nDisconnected from server')
            sys.exit()
        else:
            print('server -> ',data.decode('utf-8'))
            msg = input('client : ')
            self.client.send(msg.encode())
            sys.stdout.flush()

    def save_data(self,data: bytes) -> None:
        with open('received_file.txt',mode="wb") as f:
            f.write(data)


if __name__ == '__main__':
    req = Client()
    while True:
        req.Request()
