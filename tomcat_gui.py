import tkinter as tk
from tkinter import ttk
from my_sniffer import *
from my_packet import *

# Main window.
root = tk.Tk()
root.title('Tomcat')
root.geometry('500x500')

button_sniff = tk.Button(master=root, text='Sniff', width=15)

button_sniff.pack()

# Display the GUI.
tk.mainloop()
