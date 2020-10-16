import scapy.all as scapy
import re


def start_sniff(counts):
    """
    start_sniff captures packets and calls a callback.
    :param p - Packet to capture.
    :param counts - How many packets to capture.
    :param dictionary = Dictionary of source and destination IPs.
    """
    scapy.sniff(prn=packet_callback, count=counts)


def stop_sniff():
    print('Stopping')


def get_dict(l, capture):
    """
    :param l:       List to hold IP addresses.
    :param capture: The string containing the packet.
    :return:        Dictionary of source IP addresses.
    """



# Parse the response.
def packet_callback(packet):

    # dump=True returns the packet as a string, get rid of all whitespace.
    capture = re.sub(r'[\n\t\s]', '', packet.show(dump=True))
    print(capture)
    # Find all the ip addresses regex.
    # Issue is need IPv4 addresses only. ARP and IPv6 mess it up.
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', capture)
    print(ip)


