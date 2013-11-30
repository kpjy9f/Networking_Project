__author__ = 'Kyle'

import httplib
import sys

http_server = sys.argv[1]

conn = httplib.HTTPConnection('127.0.0.1', http_server)

while 1:
    dl_file = raw_input('Please enter the file to download: ')
    if dl_file == 'exit':
        break

    conn.request('GET', dl_file)

    # catch exception on 404 error
    rsp = conn.getresponse()

    print(rsp.status, rsp.reason)
    if rsp.status == 200:
        data_received = rsp.read()
        print(data_received)
    else:
        print "problem : the query returned %s because %s" % (rsp.status, rsp.reason)

conn.close()
