import socket
import os
import struct
import binascii

def analyze_ether_header(data):
    eth_hdr = struct.unpack("!6s6sH", data[:14])
    dest_mac= binascii.hexlify(eth_hdr[0])
    dest_mac= dest_mac[:2]+":"+dest_mac[2:4]+":"+dest_mac[4:6]+":"+dest_mac[6:8]+":"+dest_mac[8:10]+":"+dest_mac[10:]
    src_mac = binascii.hexlify(eth_hdr[1])
    src_mac= src_mac[:2]+":"+src_mac[2:4]+":"+src_mac[4:6]+":"+src_mac[6:8]+":"+src_mac[8:10]+":"+src_mac[10:]
    proto   = eth_hdr[2]

    print dest_mac
    print src_mac
    print hex(proto)

    data = data[14:]
    return data

def main():
    sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0003))
    #sous MAc OS 
    recv_data = sniffer_socket.recv(2048)
    os.system("clear")
    data = analyze_ether_header(recv_data)

while True:
    main()
