#!/usr/bin/python

import scapy.all as scapy

filter = "port 31337"
iface = "eth0"

def prepare_response(t):
    print("Received: %s" % repr(t))
    t.src, t.dst = t.dst, t.src  # swap ethernet addresses
    ip = t.getlayer("IP")
    ip.src, ip.dst = ip.dst, ip.src
    t.dport, t.sport = t.sport, t.dport
    t.ack = t.seq
    t.ack += 1

syn = scapy.sniff(filter=filter, count=1, iface=iface)[0]
print(syn.sprintf('%TCP.flags%'))

syn_ack = syn
prepare_response(syn_ack)
syn_ack.getlayer("TCP").flags |= 0x10  # set the ACK flag
print(syn_ack.sprintf('%TCP.flags%'))

print("Sending: %s" % repr(syn_ack))
scapy.sendp(syn_ack, iface=iface, verbose=False)

ack = scapy.sniff(filter=filter, count=1, iface=iface)[0]
assert(ack.flags & 0x10)
