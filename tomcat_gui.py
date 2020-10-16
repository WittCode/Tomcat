import tkinter as tk
from tkinter import ttk
from my_sniffer import *
from my_packet import *

# Main window.
root = tk.Tk()
# Title of the window.
root.title('Tomcat')

# Label to display text.
label_ip = tk.Label(master=root, text='Tomcat Packet Sniffer')

# When a function is called without parentheses a function reference is sent to the callable.
# When you use the lambda command it returns a reference to the created function.
button_sniff = tk.Button(master=root, text='Sniff', width=15,
                         command= lambda: start_sniff(widget=label_ip))

button_sniff.pack(padx=10, pady=5, side=tk.LEFT)

label_ip.pack()

# Display the GUI.
tk.mainloop()