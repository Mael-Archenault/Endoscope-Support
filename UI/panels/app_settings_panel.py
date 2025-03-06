import time
from panels.panel import Panel
from customtkinter import *
import tkinter as tk
from communication import send_command
from const import *
from color import color
from PIL import Image
from languages import *

from themes import themes

class AppSettingsPanel(Panel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        

        self.appearance_frame = CTkFrame(self,
                                         width= 800,
                                         height = 600)
        self.appearance_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.appearance_label  = CTkLabel(self.appearance_frame,
                                          width = 780,
                                          corner_radius=10,
                                          font=("Roboto", 16))
        self.appearance_label.place(relx = 0.5, rely = 0.05, anchor = "center")

        self.color_theme_label = CTkLabel(self.appearance_frame,
                                          font=("Roboto", 14))
        
        self.color_theme_combobox = CTkComboBox(self.appearance_frame, 
                                               width = 200)
        
        self.color_theme_apply_button = CTkButton(self.appearance_frame,
                                                  command = self.set_new_color_theme)

        self.color_theme_label.place(relx = 0.1, rely = 0.2)
        self.color_theme_combobox.place(relx = 0.25, rely = 0.2)
        self.color_theme_apply_button.place(relx = 0.55, rely = 0.2)

        self.language_label = CTkLabel(self.appearance_frame,
                                          font=("Roboto", 14))
        


        available_languages = ["English (default)", "Français", "Deutsch", "Español", "Italiano", "中文", "日本語", "한국어"]
        
        self.language_combobox = CTkComboBox(self.appearance_frame, 
                                               width = 200,
                                               values=available_languages)
        
        self.language_apply_button = CTkButton(self.appearance_frame,
                                                  command = self.set_new_language)

        self.language_label.place(relx = 0.1, rely = 0.4)
        self.language_combobox.place(relx = 0.25, rely = 0.4)
        self.language_apply_button.place(relx = 0.55, rely = 0.4)


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
        
        self.language_label.configure(
                                        fg_color = "transparent",
                                        text_color = colors["section_text_color"])
        self.language_combobox.configure(
                                        fg_color = colors["combobox_fg"],
                                        text_color = colors["combobox_text_color"],
                                        border_color = colors["combobox_border"],
                                        button_color = colors["combobox_button"],
                                        dropdown_fg_color= colors["combobox_dropdown_fg"],
                                        
                                        dropdown_text_color= colors["combobox_dropdown_text_color"],
                                        
                                        dropdown_hover_color = colors["combobox_dropdown_hover"],
                                       
                                        button_hover_color = colors["combobox_button_hover"])
        
        self.language_apply_button.configure(
                                        fg_color = colors["blue_button"],
                                        hover_color = colors["blue_button_hover"])
    def set_new_color_theme(self):
        theme = self.color_theme_combobox.get()

        language = languages[self.app.language]
        for key in language.keys():
            if language[key]== theme:
                theme_in_english = key

        self.app.set_theme(theme_in_english)

    def set_new_language(self):
        name = self.language_combobox.get()
        self.app.set_language(name)

    def set_language(self, name):
        language = languages[name]

        self.title.configure(text = language["App Settings"])
        self.appearance_label.configure(text = language["Appearance"])
        self.color_theme_label.configure(text = language["Color Theme"] + " :")

        themes = [language["Dark (default)"], language["Light"], language["Oceanic"], language["Emerald Forest"], language["Violet Night"], language["Solar Flare"]]
        self.color_theme_combobox.configure(values = themes)
        self.color_theme_combobox.set(language["Dark (default)"])
        self.color_theme_apply_button.configure(text = language["Apply"])


        self.language_label.configure(text = language["Language"] + " :")

        
        self.language_combobox.set(name)
        self.language_apply_button.configure(text = language["Apply"])