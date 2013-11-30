__author__ = 'Kyle'

import MyTCP
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
root_dir = './Origin/'


def get_current_mills():
    return int(round(time.time() * 1000))


class Sender:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        self.myTCP_socket = MyTCP.MyTCPSocket()
        self.myTCP_socket.bind(self.host, self.port)
        self.myTCP_socket.listen()
        print 'Successfully connected'
        while True:
            file_name = self.myTCP_socket.receive()
            print 'Received request of ', file_name
            print 'Sending file ', root_dir + file_name, '...'
            try:
                f = open(root_dir + file_name, 'rb')
                data_out = f.read()
                self.myTCP_socket.send(data_out) # currently sending to self because of hardcoded nonsense

                f.close()
                print 'Successfully closed'
                print 'File Sent!!'

            except Exception as e:
                print e

            except IOError:
                print 'File not found! '
                #self.myTCP_socket.send_error(404, 'File Not Found: %s' % data)


if __name__ == '__main__':
    print 'Starting listening on: ', UDP_IP, ' port: ', str(UDP_PORT)
    Sender(UDP_IP, UDP_PORT).start()