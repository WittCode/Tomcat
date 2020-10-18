import tkinter as tk
import scapy.all as scapy
from packet_process import *

# Main window.
root = tk.Tk()
root.title('Tomcat')
root.geometry('500x500')

button_sniff = tk.Button(master=root, text='Sniff', width=15,
                         command=lambda: scapy.sniff(prn=custom_action(root),
                                                     count=1))
button_sniff.pack()

# Display the GUI.
tk.mainloop()
