__author__ = 'Kyle'

import MyTCP
import sys
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
root_dir = './Proxy/'


def get_current_mills():
    return int(round(time.time() * 1000))


class Receiver:
    def __init__(self, host):
        self.host = host
        self.file_name = None
        self.myTCP_socket = None

    def request(self, file_name):
        self.file_name = file_name
        self.myTCP_socket = MyTCP.MyTCPSocket()
        self.myTCP_socket.connect(UDP_IP, UDP_PORT)
        self.myTCP_socket.send(self.file_name)

    def receive(self):
        result = self.myTCP_socket.receive()
        return result

    def close(self):
        self.myTCP_socket.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test = Receiver(UDP_IP)

        print 'Requesting file ', sys.argv[1]
        test.request(sys.argv[1])

        print 'Receiving result ... '
        data = test.receive()

        print 'Writing file "', sys.argv[1], '"'
        f = open(root_dir + sys.argv[1], 'wb')
        f.write(data)
        f.close()
        print 'Successfully closed'

        print 'File received'
        test.close()