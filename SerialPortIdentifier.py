
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright(c) 2022 Pierre Quélin <pierre.quelin.1972@gmail.com>
#
# Author: Pierre Quélin
# Date created: 25/03/2022
# Python Version: 3.9

from serial import Serial, SerialException
from serial.tools import list_ports

from tkinter import *
from time import sleep, time

from threading import Thread, Lock

import os
import sys

SERIAL_TIMEOUT = 0.3

# bypass pyinstaller path
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Serport:
    def __init__(self, dev, desc):
        self._dev = dev
        self._desc = desc
        self._state = False
        self._lock = Lock()
        self._running = True
        self._thread = Thread(target=self.run)#, args =(self,))
        self._thread.start()

    def isReady(self):
        self._lock.acquire()
        state = self._state
        self._lock.release()
        return state

    def terminate(self):
        self._running = False
        self._thread.join()

    def run(self):
        while(self._running):
            start = time()
  
            try:
                s = Serial(self._dev, timeout=SERIAL_TIMEOUT)
                s.reset_input_buffer()
                s.reset_output_buffer()
                ping = "boomerang".encode()
                s.write(ping)
                pong = s.read(len(ping))
                s.close()
                self._lock.acquire()
                self._state = ping == pong
                self._lock.release()
            except SerialException:
                self._lock.acquire()
                self._state = False
                self._lock.release()
              
            stop = time()
            delay = SERIAL_TIMEOUT - (stop-start)
            if delay > 0:
                sleep(delay)

class MainApplication(Tk):
    def __init__(self):
        super().__init__()
        #icon = PhotoImage(file=resource_path('serial.png'))
        #self.iconphoto('False', icon)
        self.title('Serial Identifier')

        self._serports = []
        self._checkbuttons = []

        self.create_widgets()
        
        self.geometry("") # resize
        self.resizable(width=False, height=False) # disable resizable

    def create_widgets(self):
        for (dev, desc, unused) in sorted(list_ports.comports()):
            # Ports
            self._serports.append(Serport(dev, desc))
            # Buttons
            self._checkbuttons.append(Checkbutton(self.master, text=dev + "\n" + desc,
                              justify=LEFT,
                              pady=5,
                              # state=DISABLED,
                              height = 2)) # 2 lines
            self._checkbuttons[-1].deselect()
            self._checkbuttons[-1].pack( anchor="w" ) # Align left

            self.after(300, self.check, self._serports[-1], self._checkbuttons[-1])

    def check(self, serport, checkbutton):
        if serport.isReady():
            checkbutton.select()
        else:
            checkbutton.deselect()

        self.after(300, self.check, serport, checkbutton)
    
    def destroy(self):
        for serport in self._serports:
            serport.terminate()
        super().destroy()

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
