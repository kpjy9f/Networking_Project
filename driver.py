__author__ = 'Kyle'

import os
import platform

if platform.system() == 'Windows':
    os.system("start pypy.exe ProxyServer.py")
    os.system("start pypy.exe")
