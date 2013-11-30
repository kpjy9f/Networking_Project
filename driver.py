__author__ = 'Kyle'

import os
import platform

if platform.system() == 'Windows':
    #os.system("start python.exe ProxyServer.py")
    #os.system("start python.exe -m SimpleHTTPServer 8080")
    #os.system("start python.exe myHTTPClient.py 8080")
    os.system("start python.exe MyTCPSender.py")
    os.system("start python.exe MyTCPReceiver.py")