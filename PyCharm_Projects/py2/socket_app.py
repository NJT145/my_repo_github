#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference sources:
# https://realpython.com/python-sockets/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.tutorialspoint.com/python3/python_gui_programming.htm
"""
import socket
import Tkinter as tk


class project(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.var = tk.IntVar()
        self.var.set(1)
        self.connect_role = None

        self.initgui()

    def initgui(self):
        self.grid()

        # frame_base: Contains all initial parts
        self.frame1 = tk.Frame(self, relief=tk.GROOVE)
        self.frame1.config(width=50, bg='gray91')
        self.frame1.grid(row=0, column=0, rowspan=4, columnspan=4, padx=3, pady=3)

        # label1_base: Title bar
        self.label1_base = tk.Label(self.frame1, text='Project 2', bg='gray91', fg='black',
                                    font=('Times New Roman', 22, 'bold', 'italic'))
        self.label1_base.grid(row=0, column=0, columnspan=4, padx=3, pady=3)
        # label2_base
        self.label2_base = tk.Label(self.frame1, text='Enter Destination IP:', bg='gray91', fg='black',
                                    font=('Times New Roman', 12))
        self.label2_base.grid(row=1, column=0, columnspan=2, padx=3, pady=3)
        #
        self.entry1 = tk.Entry(self.frame1, width=25)
        self.entry1.grid(row=1, column=2, columnspan=2, padx=3, pady=3)
        # label3_base: asking for protocol type
        self.label3_base = tk.Label(self.frame1, text='Protocol:', bg='gray91', fg='black',
                                    font=('Times New Roman', 12))
        self.label3_base.grid(row=2, column=0, columnspan=2, padx=3, pady=3)
        # radiobutton1: button to select TCP
        self.radiobutton1 = tk.Radiobutton(self.frame1, text='TCP', variable=self.var, value=1, bg='gray91', fg='black',
                                           font=('Times New Roman', 11))
        self.radiobutton1.grid(row=2, column=2, padx=3, pady=3)
        # radiobutton2: button to select UDP
        self.radiobutton2 = tk.Radiobutton(self.frame1, text='UDP', variable=self.var, value=2, bg='gray91', fg='black',
                                           font=('Times New Roman', 11))
        self.radiobutton2.grid(row=2, column=3, padx=3, pady=3)
        # button_client: button to start connection
        self.button_client = tk.Button(self.frame1, text='Connect to a server =>', command=self.client_connect,
                                       font=('Times New Roman', 10), width=25, height=1, relief=tk.RAISED)
        self.button_client.grid(row=3, column=0, columnspan=2, padx=3, pady=3)
        # button_server: button to start connection
        self.button_server = tk.Button(self.frame1, text='Start server connection =>', command=self.server_connect,
                                       font=('Times New Roman', 10), width=25, height=1, relief=tk.RAISED)
        self.button_server.grid(row=3, column=2, columnspan=2, padx=3, pady=3)
        # label5_base: Connection info
        self.label5_base = tk.Label(self.frame1, text='='*40, bg='gray91', fg='black',
                               font=('Times New Roman', 12))
        self.label5_base.grid(row=4, column=0, columnspan=4, padx=3, pady=3)


    def client_connect(self):  # connection funtion for starting communication and the opening the message window
        self.connect_role = "client"
        self.label5_base.config(text='Waiting to Connection Partner', fg='red')
        selection = self.var.get()  # selection of TCP or UDP from radio button
        print selection

    def server_connect(self):  # connection funtion for starting communication and the opening the message window
        self.connect_role = "server"
        selection = self.var.get()  # selection of TCP or UDP from radio button
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
        CLIENT = self.entry1.get()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating TCP socket
        self.socket.bind((HOST, PORT))  # bind for associating the socket with adress and port number
        self.socket.listen()  # It listens for connection from client side (bin and listen is special for server only).
        self.label5_base.config(text='Waiting to Connection Partner', fg='red')
        self.conn, self.addr = self.s.accept()  # waiting for any coming connections
        if self.addr[0] != CLIENT:  # Checking if correct client IP is connected
            self.socket.close()
            return self.server_connect()
        print('Connection address:', self.addr)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            conn, addr = s.accept()
            if addr[0] != CLIENT:
                return self.server_connect()
            else:
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)


def main():
    root = tk.Tk()
    root.title("Chat Application - by Merve & Nurcan")
    root.geometry('450x180')
    root.config(background='gray91')
    app = project(root)
    root.mainloop()


if __name__ == '__main__':
    main()
