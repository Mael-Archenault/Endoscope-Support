import time
from panels.panel import Panel
from customtkinter import *
import tkinter as tk
from communication import send_command
from const import *
from color import color
from PIL import Image

class AppSettingsPanel(Panel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.title.configure(text = "App Settings")

        self.appearance_frame = CTkFrame(self,
                                         width= 800,
                                         height = 600)
        self.appearance_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.appearance_label  = CTkLabel(self.appearance_frame,
                                          width = 780,
                                          corner_radius=10,
                                          text = "Appearance",
                                          font=("Roboto", 16))
        self.appearance_label.place(relx = 0.5, rely = 0.05, anchor = "center")

        self.color_theme_label = CTkLabel(
                                          self.appearance_frame,
                                          text = "Color Theme :",
                                          font=("Roboto", 14))
        themes = ["Dark (default)", "Light", "Oceanic", "Emerald Forest", "Violet Night", "Solar Flare"]
        self.color_theme_combobox = CTkComboBox(self.appearance_frame, 
                                               values = themes,
                                               width = 200)
        
        self.color_theme_apply_button = CTkButton(self.appearance_frame,
                                                  text="Apply",
                                                  command = self.set_new_color_theme)

        self.color_theme_label.place(relx = 0.1, rely = 0.2)
        self.color_theme_combobox.place(relx = 0.25, rely = 0.2)
        self.color_theme_apply_button.place(relx = 0.55, rely = 0.2)

        # Setting the default values
        self.reset_values()


    

    def reset_values(self):
        pass

    def set_theme(self, theme):
        super().set_theme(theme)
        colors = themes[theme]

        self.appearance_frame.configure(fg_color = colors["section_bg"])
        self.appearance_label.configure(fg_color = colors["section_title"], text_color = colors["section_title_text_color"])


        self.color_theme_label.configure(
                                        fg_color = "transparent",
                                        text_color = colors["section_text_color"])
        self.color_theme_combobox.configure(
                                        fg_color = colors["combobox_fg"],
                                        text_color = colors["combobox_text_color"],
                                        border_color = colors["combobox_border"],
                                        button_color = colors["combobox_button"],
                                        dropdown_fg_color= colors["combobox_dropdown_fg"],
                                        
                                        dropdown_text_color= colors["combobox_dropdown_text_color"],
                                        
                                        dropdown_hover_color = colors["combobox_dropdown_hover"],
                                       
                                        button_hover_color = colors["combobox_button_hover"])
        
        self.color_theme_apply_button.configure(
                                        fg_color = colors["blue_button"],
                                        hover_color = colors["blue_button_hover"])
    def set_new_color_theme(self):
        theme = self.color_theme_combobox.get()
        self.app.set_theme(theme)