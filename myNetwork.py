__author__ = 'Kyle'

#import myTcp
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('testfile.txt', (UDP_IP, UDP_PORT))
