import scapy.all as scapy
import re

'''
@:param event - The clicking of the button.
'''
def start_sniff(counts):
    scapy.sniff(prn=packet_callback, count=counts)


def stop_sniff():
    print('Stopping')


# Parse the response.
def packet_callback(packet):
    # dump=True returns the packet as a string, get rid of all whitespace.
    capture = re.sub(r'[\n\t\s]', '', packet.show(dump=True))
    print(capture)

