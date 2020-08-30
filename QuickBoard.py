import tkinter as tk
from tkinter import font as tkfont
import webbrowser
import os
import time

class QuickBoard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")
        container = tk.Frame(self, height=600, width=1024, bg="blue")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = MainMenu(parent=container, controller=self)
        self.frames["MainMenu"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame = ShutdownPage(parent=container, controller=self)
        self.frames["ShutdownPage"] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def OpenYoutube(self):
        os.system("sudo xdc-open https://www.youtube.com")

    def Shutdown(self):
        self.show_frame("ShutdownPage")
        self.frames["ShutdownPage"].StartCounting()
        os.system("sudo shutdown")

    def CancelShutdown(self):
        self.show_frame("MainMenu")
        os.system("sudo shutdown -c")

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, height=600, width=1024, bg="blue")
        self.controller = controller
        self.ButtonFont = tkfont.Font(family="Helvetica", size=16, weight="bold")
        label = tk.Label(self, text="Main Menu", font=controller.title_font, bg="blue")
        label.pack(side="top")
        b1 = tk.Button(self, text="Youtube", command=lambda: controller.OpenYoutube() , font=self.ButtonFont, bg="red", height=5, width=20)
        b2 = tk.Button(self, text="Shutdown", command=lambda: controller.Shutdown(), font= self.ButtonFont, bg="gray", height=5, width=20)
        b1.pack(side="left")
        b2.pack(side="right")

class ShutdownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="gray")
        self.controller = controller
        self.counter = 0
        self.ButtonFont = tkfont.Font(family="Helvetica", size=16, weight="bold")
        label = tk.Label(self, text="System Shutting Down...", font=controller.title_font, bg="gray")
        label.pack(side="top")
        self.t1 = tk.Label(self, text="", font=self.ButtonFont)
        b1 = tk.Button(self, text="Cancel", command=lambda: controller.CancelShutdown(), font=self.ButtonFont, bg="gray", height=3, width=10)
        self.t1.pack()
        b1.pack()

    def StartCounting(self):
        self.counter = 60.0
        for x in range(600):
            self.t1["text"] = "shutting down after "+str(round(self.counter, 0))+" seconds"
            time.sleep(0.1)
            tk.Tk.update(self)
            self.counter-= 0.1


if __name__=="__main__":
    app = QuickBoard()
    app.mainloop()