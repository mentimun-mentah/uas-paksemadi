import socket

class Server:
    _HOST = socket.gethostbyname("localhost")
    _PORT = 8081

    @classmethod
    def Listen(self) -> bytes:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
            # to reuse address again
            serve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serve.bind((self._HOST,self._PORT))
            serve.listen()
            conn, addr = serve.accept()
            with conn:
                while (data := conn.recv(1024)):
                    print('client -> ',data.decode('utf-8'))
                    text = input('server : ')
                    conn.send(text.encode())


if __name__ == '__main__':
    print("====== waiting client ======\n")
    while True:
        Server.Listen()
