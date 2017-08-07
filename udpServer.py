import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = str(data.decode())
        print("message from: {}".format(str(addr)))
        print("from connected user: {}".format(data))
        data = data.upper()
        print("sending: {}".format(data))

        s.sendto(data.encode(), addr)

    s.close()

if __name__ == '__main__':
    Main()