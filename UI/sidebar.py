from customtkinter import *
from const import *

from PIL import Image

class Sidebar(CTkFrame):
    def __init__(self, master, panel_container):
        super().__init__(master)


        self.width = SIDEBAR_WIDTH
        self.button_height = 100
        self.button_spacing = 10


        self.configure(width=self.width,
                            height = WINDOW_HEIGHT,
                            corner_radius=0,
                           )

        self.panel_container= panel_container
    

        self.buttons = [
            {"name": "Connection", "icon": "usb_icon.png", "command": lambda:self.panel_container.setPanel("Connection")},
            {"name": "Test", "icon": "test_icon.png", "command": lambda:self.panel_container.setPanel("Test")},
            {"name": "Capture\nSettings", "icon": "settings_icon.png", "command": lambda:self.panel_container.setPanel("Settings")},
            {"name": "Capture", "icon": "capture_icon.png", "command": lambda:self.panel_container.setPanel("Capture")},
            ]
        for i in range(len(self.buttons)):
            element = self.buttons[i]
            image = Image.open("./img/"+element["icon"])
            icon = CTkImage(light_image = image,
                            dark_image=image,
                            size=(int(self.button_height*0.6),
                            int(self.button_height*0.6)))
            

            button = CTkButton(self,
                               width = self.width*0.8,
                               height = self.button_height,
                               corner_radius= 10,
                               text=element["name"],
                               image=icon,
                               compound="top",
                               command = element["command"],
                               font=("Roboto", 16),
                               text_color="#D9D9D9",
                               fg_color = "#2B2B2B",
                               hover_color="gray30")

            button.place(relx = 0.5, rely = 0.2 + i*0.2, anchor = "center")
