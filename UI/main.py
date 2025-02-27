from customtkinter import *

from panels.panel_container import PanelContainer
from sidebar import Sidebar

from const import *

import time

from PIL import Image
from communication import receive_data


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Endoscope Application")
        self.geometry(str(WINDOW_WIDTH)+ "x"+ str(WINDOW_HEIGHT))
        self.resizable(False, False)

        self.panel_container = PanelContainer(self)
        self.panel_container.place(x = 100, y = 0)

        self.sidebar = Sidebar(self, self.panel_container)
        self.sidebar.place(x = 0, y = 0)


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
app.mainloop()  