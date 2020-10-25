import tkinter as tk
from tkinter import ttk
import scapy.all as scapy
import threading
import collections
import socket


# --- functions ---


def sniffing():
    print('Starting!')
    scapy.sniff(prn=custom_action(root), stop_filter=stop_sniffing)


def custom_action(r):
    def packet_callback(packet):
        # Dictionary where key is local IP and value is source.
        global d
        global treev

        # Check if packet has IP layer.
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            # If source IP in subdomain continue.
            if src_ip[0:9] == '192.168.0':
                # If source IP is not registered, register it and add destination.
                if src_ip not in d:
                    # Add to dictionary.
                    d[src_ip].append(dst_ip)
                    print(dst_ip)
                    try:
                        print(socket.gethostbyaddr(dst_ip))
                    except socket.herror:
                        print('Not found.')
                    row = treev.insert('', index=tk.END, text=src_ip)
                    # Append to parent row.
                    treev.insert(row, tk.END, text=dst_ip)
                    treev.pack(fill=tk.X)
                # If source IP is registered check if destination is registered.
                else:
                    # If destination IP isn't registered with source IP add it.
                    if dst_ip not in d[src_ip]:
                        d[src_ip].append(dst_ip)
                        cur_item = treev.focus()
                        print(dst_ip)
                        try:
                            print(socket.gethostbyaddr(dst_ip))
                        except socket.herror:
                            print('Not found.')
                        if treev.item(cur_item)['text'] == src_ip:
                            treev.insert(cur_item, tk.END, text=dst_ip)




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

socket.setdefaulttimeout(1.0)

root = tk.Tk()
root.geometry('500x500')
root.title('Tomcat')

treev = ttk.Treeview(root, height=400)
treev.column('#0', width=50, minwidth=25)

button_frame = tk.Frame(root)

tk.Button(button_frame, text="Start sniffing", command=start_button, width=15).pack(side=tk.LEFT)
tk.Button(button_frame, text="Stop sniffing", command=stop_button, width=15).pack(side=tk.LEFT)

button_frame.pack(side=tk.BOTTOM)

root.mainloop()
