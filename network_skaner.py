#!/usr/bin/env python

import scapy.all as scapy
from tabulate import tabulate
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = map(lambda answer_list: {"IP": answer_list[1].psrc, "Mac Adress": answer_list[1].hwsrc}, answer_list)
    return list(clients_list)

def print_rezult(clients_list):
    rezult_list = tabulate(clients_list, headers='keys', tablefmt='pipe', stralign='center')
    print(rezult_list)

if __name__ == "__main__":

    options = get_arguments()
    scan_result = scan(options.target)
    print_rezult(scan_result)
