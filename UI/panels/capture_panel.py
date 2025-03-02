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

class CapturePanel(Panel):
    def __init__(self, master):
        super().__init__(master)

        self.total_time = 0
        self.time = 0
        self.state = "STOPPED"

        
        ## Box for the section "Control of the capture"
        self.control_frame = CTkFrame(self,
                                        width = 400,
                                        height = 200)
        self.control_frame.place(relx = 0.24, rely = 0.22, anchor = "center")

        self.control_label = CTkLabel(self.control_frame,
                                         font=("Roboto", 16),
                                         width = 380,
                                         corner_radius=10)
        self.control_label.place(relx = 0.5, rely = 0.1, anchor = "center")

        self.transparent_buttons = []
        self.control_buttons = [
            {"name": "Play", "icon": "play_icon.png", "command": self.play},
            {"name": "Pause", "icon": "pause_icon.png", "command": self.pause},
            {"name": "Stop", "icon": "stop_icon.png", "command": self.stop}
            ]
        for i in range(len(self.control_buttons)):
            element = self.control_buttons[i]
            
            image = Image.open("./img/"+element["icon"])
            icon = CTkImage(light_image = image,
                                dark_image=image,
                                size=(75,75))
                

            button = CTkButton(self.control_frame,
                                corner_radius= 10,
                                width = 75,
                                height = 75,
                                text=element["name"],
                                image=icon,
                                compound="top",
                                command = element["command"],
                                font=("Roboto", 16))
            self.transparent_buttons.append(button)
            button.place(relx = 0.2 + i*0.3, rely = 0.6, anchor = "center")
        
        ## Box for the section "Position and Angle"
        self.position_frame = CTkFrame(self,
                                        width = 400,
                                        height = 200)
        self.position_frame.place(relx = 0.24, rely = 0.52, anchor = "center")

        self.position_label = CTkLabel(self.position_frame,
                                         font=("Roboto", 16),
                                         width = 380,
                                         corner_radius=10)
        self.position_label.place(relx = 0.5, rely = 0.1, anchor = "center")

        self.x_frame = CTkFrame(self.position_frame)
        self.x_label = CTkLabel(self.x_frame, 
                                    text="x :",
                                     font=("Roboto", 16))
        self.x_value = CTkTextbox(self.x_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")
        self.x_label_mm = CTkLabel(self.x_frame, 
                                    text="mm",
                                     font=("Roboto", 16))

        self.x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.x_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.x_label_mm.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.x_frame.place(relx = 0.5, rely = 0.35, anchor = "center")

        self.theta_frame = CTkFrame(self.position_frame)
        self.theta_label = CTkLabel(self.theta_frame, 
                                    text="Theta :",
                                     font=("Roboto", 16))
        self.theta_value = CTkTextbox(self.theta_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")
        self.theta_label_degree = CTkLabel(self.theta_frame, 
                                    text="°",
                                     font=("Roboto", 16))

        self.theta_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.theta_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.theta_label_degree.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.theta_frame.place(relx = 0.5, rely = 0.7, anchor = "center")



        ## Box for the section "Status of the Capture"
        self.status_frame = CTkFrame(self,
                                        width = 550,
                                        height = 415)
        self.status_frame.place(relx = 0.69, rely = 0.37, anchor = "center")

        self.status_label = CTkLabel(self.status_frame,
                                         font=("Roboto", 16),
                                         width = 530,
                                         corner_radius=10)

        self.status_label.place(relx = 0.5, rely = 0.05, anchor = "center")

        
        self.progress_bar = CTkProgressBar(self.status_frame,
                                            height = 20,
                                            width =400)
        self.progress_percentage = CTkLabel(self.status_frame,
                                                font = ("Roboto", 15))
        self.progress_bar.place(relx = 0.45, rely = 0.2, anchor = "center")
        self.progress_percentage.place(relx = 0.9, rely = 0.2, anchor = "center")


        self.time_frame = CTkFrame(self.status_frame)
        self.time_frame.place(relx = 0.25, rely = 0.35, anchor = "center")

        self.time_label = CTkLabel(self.time_frame,
                                     font=("Roboto", 15))
        self.time_value = CTkTextbox(self.time_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")

        self.time_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.time_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.estimated_time_frame = CTkFrame(self.status_frame)
        self.estimated_time_frame.place(relx = 0.75, rely = 0.35, anchor = "center")

        self.estimated_time_label = CTkLabel(self.estimated_time_frame,
                                     font=("Roboto", 15))
        self.estimated_time_value = CTkTextbox(self.estimated_time_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")

        self.estimated_time_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.estimated_time_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.nb_pictures_frame = CTkFrame(self.status_frame)
        self.nb_pictures_frame.place(relx = 0.5, rely = 0.55, anchor = "center")

        self.nb_pictures_label = CTkLabel(self.nb_pictures_frame,
                                     font=("Roboto", 15))
        self.nb_pictures_value = CTkTextbox(self.nb_pictures_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")
        self.total_nb_pictures_label = CTkLabel(self.nb_pictures_frame, 
                                    text="/100",
                                     font=("Roboto", 15))

        self.nb_pictures_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.nb_pictures_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_nb_pictures_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.nb_pictures_angle_frame = CTkFrame(self.status_frame)
        self.nb_pictures_angle_frame.place(relx = 0.5, rely = 0.7, anchor = "center")

        self.nb_pictures_angle_label = CTkLabel(self.nb_pictures_angle_frame,
                                     font=("Roboto", 15))
        self.nb_pictures_angle_value = CTkTextbox(self.nb_pictures_angle_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")
        self.total_nb_pictures_angle_label = CTkLabel(self.nb_pictures_angle_frame, 
                                    text="/100",
                                     font=("Roboto", 15))

        self.nb_pictures_angle_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.nb_pictures_angle_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_nb_pictures_angle_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.explored_angles_frame = CTkFrame(self.status_frame)
        self.explored_angles_frame.place(relx = 0.5, rely = 0.85, anchor = "center")

        self.explored_angles_label = CTkLabel(self.explored_angles_frame,
                                     font=("Roboto", 15))
        self.explored_angles_value = CTkTextbox(self.explored_angles_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")
        self.total_explored_angles_label = CTkLabel(self.explored_angles_frame, 
                                    text="/100",
                                     font=("Roboto", 15))

        self.explored_angles_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.explored_angles_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_explored_angles_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        # Box for the logs

        self.logs_frame = CTkTextbox(self,
                                    width = 990,
                                    height = 200,
                                    font = ("Roboto", 16),
                                    state = "disabled")
        self.logs_frame.place(relx = 0.5, rely = 0.82, anchor = "center")

        # Setting the default values
        self.reset_values()


    

    def reset_values(self):
        ## Position and Angle
        self.change_value("x_value", "0 mm", "disabled")
        self.x_label_mm.configure(text = "/100 mm")

        self.change_value("theta_value", "0 °", "disabled")
        self.theta_label_degree.configure(text = "/360 °")

        ## Status of the capture
        self.progress_bar.set(0.0)
        self.progress_percentage.configure(text = "0%")

        self.change_value("time_value", "00:00:00", "disabled")
        self.change_value("estimated_time_value", "00:00:00", "disabled")

        self.change_value("nb_pictures_value", "0", "disabled")
        self.total_nb_pictures_label.configure(text = "/100")

        self.change_value("nb_pictures_angle_value", "0", "disabled")
        self.total_nb_pictures_angle_label.configure(text = "/100")

        
        self.change_value("explored_angles_value", "0", "disabled")
        self.total_explored_angles_label.configure(text = "/100")

    def play(self):

        if self.state == "STOPPED":
            self.state = "RUNNING"
            self.time = 0
            self.start_time = time.time()
            send_command("play")

        if self.state == "PAUSED":
            self.state = "RUNNING"
            print(self.time)
            print(self.start_time)
            self.start_time = time.time()-self.time
            print(self.start_time)
            send_command("play")
    def pause(self):
        if self.state == "RUNNING":
            self.state = "PAUSED"
            send_command("pause")

    def stop(self):
        if self.state == "RUNNING" or self.state=="PAUSED":
            self.state = "STOPPED"
            send_command("stop")


    def set_theme(self, theme):
        super().set_theme(theme)
        colors = themes[theme]

        self.control_frame.configure(bg_color = "transparent", fg_color = colors["section_bg"])
        self.control_label.configure(bg_color = "transparent", fg_color = colors["section_title"], text_color = colors["section_title_text_color"])
        self.position_frame.configure(bg_color = "transparent", fg_color = colors["section_bg"])
        self.position_label.configure(bg_color = "transparent", fg_color = colors["section_title"], text_color = colors["section_title_text_color"])
        self.x_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.x_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.x_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.x_label_mm.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.theta_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.theta_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.theta_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.theta_label_degree.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.status_frame.configure(bg_color = "transparent", fg_color = colors["section_bg"])
        self.status_label.configure(bg_color = "transparent", fg_color = colors["section_title"], text_color = colors["section_title_text_color"])
        self.time_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.time_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.time_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.estimated_time_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.estimated_time_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.estimated_time_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.nb_pictures_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.nb_pictures_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.nb_pictures_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.total_nb_pictures_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.nb_pictures_angle_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.nb_pictures_angle_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.nb_pictures_angle_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.total_nb_pictures_angle_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.explored_angles_frame.configure(bg_color = "transparent", fg_color = colors["sub_section_bg"])
        self.explored_angles_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.explored_angles_value.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])
        self.total_explored_angles_label.configure(bg_color = "transparent", fg_color = "transparent", text_color = colors["sub_section_text_color"])
        self.logs_frame.configure(bg_color = "transparent", fg_color = colors["textbox_bg"], text_color = colors["textbox_text_color"])


        self.control_buttons = [
            {"name": "Play", "icon": "play_icon.png", "command": self.play},
            {"name": "Pause", "icon": "pause_icon.png", "command": self.pause},
            {"name": "Stop", "icon": "stop_icon.png", "command": self.stop}
            ]
        
        for i in range(len(self.control_buttons)):
            element = self.control_buttons[i]
            
            if (i < 2):
                image = Image.open("./img/"+element["icon"])
                image = color(image, colors["control_button"])
                icon = CTkImage(light_image = image,
                                    dark_image=image,
                                    size=(75,75))
                self.transparent_buttons[i].configure(image=icon)
    
            self.transparent_buttons[i].configure(bg_color = "transparent", fg_color = "transparent",hover_color = colors["section_button_hover"],text_color=colors["section_text_color"])


            self.progress_bar.configure(fg_color = colors["progressbar_fg"], progress_color = colors["progressbar_color"])
            self.progress_percentage.configure(text_color = colors["section_text_color"])

    def set_language(self, name):
        language = languages[name]
        self.title.configure(text=language["Capture"])
        self.control_label.configure(text=language["Control"])
        self.position_label.configure(text=language["Position and Angle"])
        self.status_label.configure(text=language["Capture Status"])
        self.time_label.configure(text=language["Capture Time"])
        self.estimated_time_label.configure(text=language["Estimated Time\nLeft"])
        self.nb_pictures_label.configure(text=language["Number of Pictures Captured"] + " :")
        self.nb_pictures_angle_label.configure(text=language["Number of Pictures for this Angle"]+ " :")
        self.explored_angles_label.configure(text=language["Number of Angles Completed"]+ " :")