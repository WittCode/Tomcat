import tkinter as tk
from my_sniffer import *

# Main window.
root = tk.Tk()
# Title of the window.
root.title('Tomcat')

# Frames to hold the top, middle, and bottom widgets.
frame_top = tk.Frame(master=root)
frame_mid = tk.Frame(master=root)
frame_bottom = tk.Frame(master=root)

# When a function is called without parentheses a function reference is sent to the callable.
button_sniff = tk.Button(master=frame_bottom, text='Sniff', width=15)
button_sniff.bind(sequence='<Button-1>', func=start_sniff)
button_stop = tk.Button(master=frame_bottom, text='Stop', command=stop_sniff, width=15)
button_sniff.pack(padx=10, pady=5, side=tk.LEFT)
button_stop.pack(padx=10, pady=5)

lb_packet_capture = tk.Listbox(master=frame_mid)
# If you start out with a keyword argument the rest of your arguments must be keyword arguments.
# Other way around is fine though.
# If you add a * before the parameter name in the function, you don't know how many arguments will be passed.
for i in range(100):
    lb_packet_capture.insert(tk.END, 'Packet ' + str(i))
lb_packet_capture.pack(fill=tk.BOTH, expand=True)

# Label to display text.
label_title = tk.Label(master=frame_top, text='Tomcat Packet Sniffer')
label_title.pack()

frame_top.pack()
frame_mid.pack(fill=tk.BOTH, expand=True)
frame_bottom.pack()

# Display the GUI.
tk.mainloop()