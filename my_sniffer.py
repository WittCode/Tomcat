import scapy.all as scapy
import io
import sys
'''
@:param event - The clicking of the button.
'''
def start_sniff(counts):
    scapy.sniff(prn=packet_callback, count=counts)


def stop_sniff():
    print('Stopping')


# Parse the response.
def packet_callback(packet):
    capture = packet.show(dump=True)
    to_parse = capture.replace(' ', '')
    parse_two = to_parse.replace('\n', '')
    print('SOCCER:\n' + parse_two)

