import scapy.all as scapy
import re


def start_sniff(widget):
    """
    start_sniff captures packets and calls a callback.
    :param p - Packet to capture.
    :param counts - How many packets to capture.
    :param dictionary = Dictionary of source and destination IPs.
    """
    scapy.sniff(prn=packet_callback, stop_filter=stop_sniff)


def stop_sniff(packet):
    """
    # Function to check whether sniffing should stop.
    :param packet: The packet we can use to check if we should stop.
    :return: True to stop sniffing.
    """
    return True


def create_dict(ip_1, ip_2):
    """
    :param ip_2:
    :param ip_1:
    :return:        Dictionary of source IP addresses.
    """
    return {'src': ip_1,
            'dst': ip_2}


def packet_callback(packet):
    """
    Called when a packet is sniffed. Parse the packet and return IP addresses.
    :param packet: Packet that was sniffed.
    :return: List of IP addresses.
    """
    print(type(packet))
    # dump=True returns the packet as a string, get rid of all whitespace.
    capture = re.sub(r'[\n\t\s]', '', packet.show(dump=True))
    if ('type=IPv4' in capture):
        print("IPv4")
        # Find all the ip addresses regex.
        # Issue is need IPv4 addresses only. ARP and IPv6 mess it up.
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', capture)
        # Pass the IPs to create dict.
        d = {'src': ip[0],
             'dst': ip[1]}
        print(d)
