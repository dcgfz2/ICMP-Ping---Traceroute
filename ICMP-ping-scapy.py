#!/usr/bin/env python3

import os
import time
from scapy.all import *

dest = sys.argv[1]

packet = IP(dst=str(dest))/ICMP()

while True:
    sendT = time.time()
    recv = sr1(packet,timeout = 2, verbose = 0)
    recvT = time.time()

    print(str(len(recv)) + " bytes from " + str(recv.src) + ": type" + str(recv.type))
    print('time = ' + str(recvT - sendT) + 's\n')

    time.sleep(1)
