from customtkinter import *
import tkinter as tk
import time
from const import *
from themes import themes


class Panel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.width = (WINDOW_WIDTH-SIDEBAR_WIDTH)*0.97
        self.height = WINDOW_HEIGHT*0.97
        self.x, self.y = 0,0
        self.title = CTkLabel(self,width=self.width*0.97,
                                text="",
                                corner_radius=6,
                                font=("Roboto", 20))
        self.title.place(relx =0.5, y = 50/2, anchor = "center")
        self.place(x=self.x,y=self.y)
        self.configure(width=self.width, height=self.height, corner_radius = 20)
        self.logs_frame = CTkTextbox(self)

    def display_log(self, message):
        # Get the current time as seconds since epoch
        current_time = time.time()

        # Get formatted local time
        local_time = time.localtime()
        formatted_time = time.strftime("%H:%M:%S", local_time)

        self.logs_frame.configure(state = "normal")
        self.logs_frame.insert(tk.END, formatted_time)

        self.logs_frame.insert(tk.END, "  ||  " + message + "\n")
        self.logs_frame.see(tk.END)
        self.logs_frame.configure(state = "disabled")
    
    def change_value(self,textbox, value, state):
        attr = getattr(self,textbox)
        if state == "disabled":
            attr.configure(state = "normal")
            
        attr.delete("1.0", tk.END)
        attr.insert("1.0", value)

        if state == "disabled":
            attr.configure(state = "disabled")

    def set_theme(self, theme):
        colors = themes[theme]
        self.configure(bg_color=colors["window_bg"], fg_color=colors["panel_bg"])
        self.title.configure(fg_color = colors["panel_title"],text_color=colors["panel_title_text_color"])
        self.logs_frame.configure(bg_color=colors["textbox_bg"], fg_color=colors["textbox_text_color"])


