from customtkinter import *

from panels.panel_container import PanelContainer
from sidebar import Sidebar

from const import *

import time

from PIL import Image
from communication import receive_data

from themes import themes

import PIL



class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Endoscope Application")

        # Setting all the background colors to transparent (we don't need them, we use foreground color)
        for widget in self.winfo_children():
            widget.configure(bg_color="transparent")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2

        self.geometry(str(WINDOW_WIDTH)+ "x"+ str(WINDOW_HEIGHT) +"+"+ str(x)+"+"+str(y))
        self.resizable(False, False)

        self.panel_container = PanelContainer(self)
        self.panel_container.place(x = 100, y = 0)

        self.sidebar = Sidebar(self, self.panel_container)
        self.sidebar.place(x = 0, y = 0)
        

        self.language = "Français"


        
    
    def set_theme(self, theme):
        colors = themes[theme]
        self.withdraw()
        self.configure(fg_color=colors["window_bg"])
        self.panel_container.set_theme(theme)
        self.sidebar.set_theme(theme)
        self.deiconify()

    def set_language(self, name):
        self.language = name
        self.sidebar.set_language(name)
        self.panel_container.set_language(name)


def update():

    
    data = receive_data()
    
    if data!=None:
        # Update the panel_container with the new data
        app.panel_container.update_data(data)
    


    capture = app.panel_container.panels["Capture"]
    if capture.state == "RUNNING":

        
        capture.time = time.time()-capture.start_time

        capture.time_left = max(0, capture.total_time - capture.time)
        local_time = capture.time

        hours = int(local_time/3600)
        local_time%=3600
        minutes = int(local_time/60)
        local_time%=60
        seconds = int(local_time)

        
        capture.change_value("time_value", str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2), "disabled")


        local_time = capture.time_left

        hours = int(local_time/3600)
        local_time%=3600
        minutes = int(local_time/60)
        local_time%=60
        seconds = int(local_time)

        capture.change_value("estimated_time_value", str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2), "disabled")
        
    app.after(UPDATE_PERIOD, update)




app = App()

app.after(UPDATE_PERIOD, update)
app.after(0, lambda : app.set_theme("Dark (default)"))
app.after(0, lambda : app.set_language("English (default)"))
app.mainloop()  