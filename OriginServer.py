__author__ = 'Kyle'

import MyTCP

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
root_dir = './Origin/'

try:
    sock = MyTCP.create_socket(UDP_IP, UDP_PORT)

    while True:
        data, addr = sock.recvfrom(1024)
        print 'received message: ', data
        print 'Sending file', data, '...'
        try:
            f = open(root_dir + data, 'rb')

            data_out = f.read()
            sock.sendto(data_out, addr)
            f.close()

        except IOError:
            print "oops"

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    sock.socket.close()