from customtkinter import *
from const import *
from color import color
from languages import *
from themes import themes

from PIL import Image

class Sidebar(CTkFrame):
    def __init__(self, master, panel_container):
        super().__init__(master)

        self.width = SIDEBAR_WIDTH
        self.button_height = 100
        self.button_spacing = 10


        self.configure(width=self.width,
                            height = WINDOW_HEIGHT,
                            corner_radius=0)

        self.panel_container= panel_container
    
        
        self.buttons = [
            {"command" : lambda:self.panel_container.setPanel("App Settings")},
            {"command": lambda:self.panel_container.setPanel("Connection")},
            {"command": lambda:self.panel_container.setPanel("Test")},
            {"command": lambda:self.panel_container.setPanel("Settings")},
            {"command": lambda:self.panel_container.setPanel("Capture")},
            ]
        
        self.transparent_buttons = []
        for i in range(len(self.buttons)):
            element = self.buttons[i]
            button = CTkButton(self,
                               width = self.width*0.8,
                               height = self.button_height,
                               corner_radius= 10,
                               compound="top",
                               command = element["command"],
                               font=("Roboto", 16))

            button.place(relx = 0.5, rely = 0.15 + i*0.17, anchor = "center")
            self.transparent_buttons.append(button)


    def set_theme(self, theme):
        colors = themes[theme]
        self.configure(bg_color = "transparent",fg_color=colors["window_bg"])

        self.buttons = [
            {"icon": "settings_icon.png"},
            {"icon": "usb_icon.png"},
            {"icon": "test_icon.png"},
            {"icon": "capture_settings_icon.png"},
            {"icon": "capture_icon.png"},
            ]
        
        

        for i in range(len(self.buttons)):
            element = self.buttons[i]
            image = Image.open("./img/"+element["icon"])
            image = color(image, colors["sidebar_icon_color"])
            icon = CTkImage(light_image = image,
                            dark_image=image,
                            size=(int(self.button_height*0.6),
                            int(self.button_height*0.6)))
            self.transparent_buttons[i].configure(bg_color = "transparent",text_color=colors["sidebar_text_color"], fg_color = "transparent", hover_color=colors["sidebar_button_hover"], image=icon)


    def set_language(self, name):
        language = languages[name]
        self.buttons = [
            {"name": language["App\nSettings"]},
            {"name": language["Connection"]},
            {"name": language["Test"]},
            {"name": language["Capture\nSettings"]},
            {"name": language["Capture"]},
            ]
        
        

        for i in range(len(self.buttons)):
            name = self.buttons[i]["name"]
            self.transparent_buttons[i].configure(text = name)

