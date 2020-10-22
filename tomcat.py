import tkinter as tk
import scapy.all as scapy
import threading
import collections


# --- functions ---


def sniffing():
    print('Starting!')
    scapy.sniff(prn=custom_action(root), stop_filter=stop_sniffing)


def custom_action(r):
    def packet_callback(packet):
        # Dictionary where key is local IP and value is source.
        global d

        # Check if packet has IP layer.
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            # If source IP in subdomain continue.
            if src_ip[0:9] == '192.168.0':
                # If source IP is not registered, register it and add destination.
                if src_ip not in d:
                    d[src_ip].append(dst_ip)
                    label = tk.Label(r)
                    label.config(text='Source IP: {}\nDestination IPs: {}'.format(src_ip, d[src_ip]))
                    label.pack()
                # If source IP is registered check if destination is registered.
                else:
                    # If destination IP isn't registered with source IP add it.
                    if dst_ip not in d[src_ip]:
                        d[src_ip].append(dst_ip)
                        label = tk.Label(r)
                        label.config(text='Source IP: {}\nDestination IPs: {}'.format(src_ip, d[src_ip]))
                        label.pack()

    return packet_callback


def stop_sniffing(packet):
    global switch
    return switch


def start_button():
    global switch
    global thread

    if (thread is None) or (not thread.is_alive()):
        switch = False
        thread = threading.Thread(target=sniffing)
        thread.start()


def stop_button():
    global switch

    switch = True


# --- main ---


thread = None
switch = False
d = collections.defaultdict(list)

root = tk.Tk()
root.geometry('500x500')
root.title('Tomcat')

tk.Button(root, text="Start sniffing", command=start_button, width=15).pack()
tk.Button(root, text="Stop sniffing", command=stop_button, width=15).pack()

root.mainloop()
