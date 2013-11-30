__author__ = 'Kyle'

import MyTCP
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

UDP_IP = '127.0.0.1'
UDP_PORT = 5005

#This class will handles any incoming request from the browser


class MyHandler(BaseHTTPRequestHandler):

#Handler for the GET requests
    def do_GET(self):
        root_dir = './Proxy/'

        try:
            #Check the file extension required and set the right mime type
            if self.path.endswith(".html"):
                mime_type = 'text/html'
                send_reply = True
            elif self.path.endswith(".txt"):
                mime_type = 'text/plain'
                send_reply = True
            elif self.path.endswith(".jpg"):
                mime_type = 'image/jpg'
                send_reply = True
            elif self.path.endswith(".gif"):
                mime_type = 'image/gif'
                send_reply = True
            elif self.path.endswith(".js"):
                mime_type = 'application/javascript'
                send_reply = True
            elif self.path.endswith(".css"):
                mime_type = 'text/css'
                send_reply = True
            elif self.path.endswith(".pdf"):
                mime_type = 'application/pdf'
                send_reply = True
            else:
                mime_type = 'text/plain'
                send_reply = False

            if send_reply:
                #Open the static file requested and send it
                #f = open(curdir + sep + self.path, 'rb')
                f = open(root_dir + self.path, 'rb')

                self.send_response(200)

                self.send_header('Content-type', mime_type)
                self.end_headers()

                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            #Request file from origin server and wait for response
            sock = MyTCP.create_socket(UDP_IP)
            sock.sendto(self.path, (UDP_IP, UDP_PORT))

            data, addr = sock.recvfrom(1024)

            f = open(root_dir + self.path, 'wb')
            f.write(data)
            f.close()
            print 'file received'
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('127.0.0.1', PORT_NUMBER), MyHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()