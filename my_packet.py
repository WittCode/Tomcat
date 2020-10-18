import scapy.all as scapy
import re
import tkinter as tk


class MyPacket(tk.Frame):
    """
    Each object of this class is a label with a source and destination
    IP address.
    """

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.src_ip = tk.StringVar()
        self.dst_ip = tk.StringVar()

        self.label_src_ip = tk.Label(self, root, textvariable=self.src_ip)
        self.label_dst_ip = tk.Label(self, root, textvariable=self.dst_ip)

    def start_sniff(self):
        scapy.sniff(prn=self.packet_callback, stop_filter=self.stop_sniff)

    def stop_sniff(self, packet):
        """
        # Function to check whether sniffing should stop.
        :param packet: The packet we can use to check if we should stop.
        :return: True to stop sniffing.
        """
        return True

    def packet_callback(self, packet):
        """
        Called when a packet is sniffed. Parse the packet and return IP addresses.
        :param packet: Packet that was sniffed.
        :return: List of IP addresses.
        """
        # dump=True returns the packet as a string, get rid of all whitespace.
        capture = re.sub(r'[\n\t\s]', '', packet.show(dump=True))
        if ('type=IPv4' in capture):
            # Find all the ip addresses regex.
            # Issue is need IPv4 addresses only. ARP and IPv6 mess it up.
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', capture)
            self.src_ip = ip[0]
            self.dst_ip = ip[1]
