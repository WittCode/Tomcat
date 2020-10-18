import tkinter as tk
import scapy.all as scapy
import threading
import re

# --- functions ---


def sniffing():
    print('Starting!')
    scapy.sniff(prn=custom_action(root), stop_filter=stop_sniffing)


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
            if src_ip[0:3] == '192' and src_ip not in d.values():
                d['src: {}'.format(i)] = src_ip
                i += 1
                print(d)
                label = tk.Label(root)
                label.config(text='Source: {}\n'
                                  'Destination: {}'.format(src_ip, dst_ip))
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
d = {}
i = 0

root = tk.Tk()
root.geometry('500x500')
root.title('Tomcat')

tk.Button(root, text="Start sniffing", command=start_button, width=15).pack()
tk.Button(root, text="Stop sniffing", command=stop_button, width=15).pack()

root.mainloop()



