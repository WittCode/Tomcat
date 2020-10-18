import re
import tkinter as tk

d = {}
i = 0


def custom_action(root):
    def packet_callback(packet):

        capture = re.sub(r'[\n\t\s]', '', packet.show(dump=True))
        if ('type=IPv4' in capture):
            global i
            global d
            # Find all the ip addresses regex.
            # Issue is need IPv4 addresses only. ARP and IPv6 mess it up.
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', capture)
            src_ip = ip[0]
            dst_ip = ip[1]
            if src_ip not in d.values():
                d['src: {}'.format(i)] = src_ip
                i += 1
                print(d)
                label = tk.Label(root)
                label.config(text='Source: {}\n'
                                  'Destination: {}'.format(src_ip, dst_ip))
                label.pack()

    return packet_callback
