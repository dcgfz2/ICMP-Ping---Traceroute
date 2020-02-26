#!/usr/bin/env python3

import os
import time
from scapy.all import *

dest = sys.argv[1]

maxHop = 30

for p in range(1,maxHop):
    packet = IP(dst = str(dest), ttl = p) / ICMP()
    
    if p == 1:
        timeSent = time.time()

    recv = sr1(packet, verbose = 0,timeout = 3)
    timeRecv = time.time()

    if recv is None:
        print(str(p) + "\t****REQUEST TIME OUT*****")
    else:
        print(str(p) + "\trtt = " + str(timeRecv - timeSent) + "s\t" + str(recv.src))
    
    if(recv.type == 0): #stop when target is hit
        break
