import tkinter as tk
from tkinter import ttk
from my_sniffer import *
from my_packet import *

# Main window.
root = tk.Tk()
# Title of the window.
root.title('Tomcat')

frame_bottom = tk.Frame(master=root)

# When a function is called without parentheses a function reference is sent to the callable.
button_sniff = tk.Button(master=frame_bottom, text='Sniff', width=15)
button_sniff.bind(sequence='<Button-1>', func=start_sniff)
button_stop = tk.Button(master=frame_bottom, text='Stop', command=stop_sniff, width=15)
button_sniff.pack(padx=10, pady=5, side=tk.LEFT)
button_stop.pack(padx=10, pady=5)

my_tree = ttk.Treeview(master=root, selectmode=tk.BROWSE)
my_tree['columns'] = 'Source IP'

my_tree.column(column='#0', anchor=tk.W)

# Create bar at the very top.
my_tree.heading(column='#0', text='Source IP', anchor=tk.W)

# Populate the treeview.
for i in range(10):

    user = '192.168.0.{}'.format(i)
    my_tree.insert(parent='', index=tk.END, iid=i,
                   text=user)

# Label to display text.
label_title = tk.Label(master=root, text='Tomcat Packet Sniffer')

label_title.pack()
my_tree.pack()
frame_bottom.pack()

# Display the GUI.
tk.mainloop()