#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
from socket import *

def tcp_test(port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		lock.acquire()
		print("Opened Port:", port)
		lock.release()

if __name__=='__main__':
    # portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])
    
    target_ip = gethostbyname(host)

    lock = threading.Lock()

    for port in range(start_port, end_port):
        t =	threading.Thread(target=tcp_test, args=(port,))
        t.start()

    main_thread = threading.currentThread()

    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
