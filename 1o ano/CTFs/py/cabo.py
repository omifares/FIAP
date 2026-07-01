from scapy.all import *
from yenc import decode

pcap = rdpcap('CP01.pcap')
f = open('CP01.yenc','w')
for p in pcap:
    if p[ICMP].type == 8:
        f.write(''.join(str(p[Raw])))
f.close()
decode('Y01.yenc', 'B01.bin')