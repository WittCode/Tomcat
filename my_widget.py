import tkinter as tk

class MyWidget(tk.Frame):

    def __init__(self, root, ip_src):
        tk.Frame.__init__(self, root)
        self.packet_name = ip_src
        self.display_ip = tk.StringVar()

        self.label_ip = tk.Label(self, root, textvariable=self.packet_name)
