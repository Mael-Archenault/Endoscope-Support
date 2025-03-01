import time
from panels.panel import Panel
from customtkinter import *
import tkinter as tk
from communication import send_command
from const import *

from color import color

from PIL import Image

class TestPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.state = "STOPPED"
        self.title.configure(text="Test")

        ## Box for the section "Test of the Movement"

        self.movement_test_frame = CTkFrame(self)
        self.movement_test_frame.place(relx = 0.35, rely = 0.315, anchor = "center")

        self.movement_test_label = CTkLabel(self.movement_test_frame,
                                            text = "Movement Test",
                                            font=("Roboto", 20),
                                            corner_radius=10)
        self.movement_test_label.grid(row = 0, column =0, columnspan = 2, sticky = "ew", padx = 10, pady = 10)

        self.translation_frame = CTkFrame(self.movement_test_frame)
        self.translation_label = CTkLabel(self.translation_frame,
                                         text = "Translation",
                                         font=("Roboto", 16),
                                         width = 300,
                                         corner_radius=10)
        
        self.rotation_frame = CTkFrame(self.movement_test_frame)
        self.rotation_label = CTkLabel(self.rotation_frame,
                                         text = "Rotation",
                                         font=("Roboto", 16),
                                         width = 300,
                                         corner_radius=10)

        self.translation_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        self.rotation_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

        self.blue_buttons = []
        self.red_buttons = []
        self.translation_buttons = [[
            {"name": "+ 1 mm","command": lambda:send_command("move 1")},
            {"name": "+ 5 mm","command": lambda:send_command("move 5")},
            {"name": "+ 10 mm","command": lambda:send_command("move 10")},
        ],
        [
            {"name": "- 1 mm","command": lambda:send_command("move -1")},
            {"name": "- 5 mm","command": lambda:send_command("move -5")},
            {"name": "- 10 mm","command": lambda:send_command("move -10")},
        ]]

        self.rotation_buttons = [[
            {"name": "+ 1 °","command": lambda:send_command("turn 1")},
            {"name": "+ 5 °","command": lambda:send_command("turn 5")},
            {"name": "+ 10 °","command": lambda:send_command("turn 10")},
        ],
        [
            {"name": "- 1 °","command": lambda:send_command("turn -1")},
            {"name": "- 5 °","command": lambda:send_command("turn -5")},
            {"name": "- 10 °","command": lambda:send_command("turn -10")}
        ]]
                      
        for i in range(len(self.translation_buttons)):
            for j in range(len(self.translation_buttons[i])):
                button = CTkButton(self.translation_frame,
                    text = self.translation_buttons[i][j]["name"],
                    height = 50,
                    width = 100,
                    command = self.translation_buttons[i][j]["command"])
                if i == 0:
                    self.blue_buttons.append(button)
                else:
                    self.red_buttons.append(button)
                button.grid(row=j+1, column=i,padx = 10, pady = 10)

        for i in range(len(self.rotation_buttons)):
            for j in range(len(self.rotation_buttons[i])):
                button = CTkButton(self.rotation_frame,
                    text = self.rotation_buttons[i][j]["name"],
                    height = 50,
                    width = 100,
                    command = self.rotation_buttons[i][j]["command"])
                if i == 0:
                    self.blue_buttons.append(button)
                else:
                    self.red_buttons.append(button)
                button.grid(row=j+1, column=i,padx = 10, pady = 10)


        self.translation_frame.grid(row = 1, rowspan= 2, column = 0, padx = 10, pady = 10)
        self.rotation_frame.grid(row = 1,rowspan = 2,column = 1, padx = 10, pady = 10)

        ## Box for the section "Position and Angle"
        self.position_frame = CTkFrame(self,
                                        width = 340,
                                        height = 200)
        self.position_frame.place(relx = 0.8, rely = 0.22, anchor = "center")

        self.position_label = CTkLabel(self.position_frame,
                                         text="Position and Angle",
                                         font=("Roboto", 16),
                                         width = 320,
                                         corner_radius=10,)
        self.position_label.place(relx = 0.5, rely = 0.1, anchor = "center")

        self.x_frame = CTkFrame(self.position_frame)
        self.x_label = CTkLabel(self.x_frame, 
                                    text="x :",
                                     font=("Roboto", 16))
        self.x_value = CTkTextbox(self.x_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")

        self.x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.x_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.x_frame.place(relx = 0.5, rely = 0.35, anchor = "center")

        self.theta_frame = CTkFrame(self.position_frame)
        self.theta_label = CTkLabel(self.theta_frame, 
                                    text="Theta :",
                                     font=("Roboto", 16))
        self.theta_value = CTkTextbox(self.theta_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")

        self.theta_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.theta_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        

        self.theta_frame.place(relx = 0.5, rely = 0.7, anchor = "center")


        ## Section for the Move To
        self.move_to_frame = CTkFrame(self,
                                        width = 680,
                                        height = 140)
        self.move_to_frame.place(relx = 0.35, rely = 0.66, anchor = "center")

        self.move_to_label = CTkLabel(self.move_to_frame,
                                         text="Move to absolute position",
                                         font=("Roboto", 16),
                                         width = 660,
                                         corner_radius=10)
        self.move_to_label.place(relx = 0.5, rely = 0.15, anchor = "center")

        self.move_to_x_frame = CTkFrame(self.move_to_frame)
        self.move_to_x_label = CTkLabel(self.move_to_x_frame, 
                                        text="x :",
                                        font=("Roboto", 16))
        self.move_to_x_value = CTkTextbox(self.move_to_x_frame,
                                    width = 100,
                                    height=30)
        self.move_to_x_label_mm = CTkLabel(self.move_to_x_frame, 
                                    text="mm",
                                     font=("Roboto", 16))

        self.move_to_x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.move_to_x_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.move_to_x_label_mm.grid(row = 0, column = 2, padx = (5,10), pady = 10)

        self.move_to_x_frame.place(relx = 0.2, rely = 0.6, anchor = "center")

        self.move_to_theta_frame = CTkFrame(self.move_to_frame)
        self.move_to_theta_label = CTkLabel(self.move_to_theta_frame, 
                                    text="Theta :",
                                     font=("Roboto", 16))
        self.move_to_theta_value = CTkTextbox(self.move_to_theta_frame,
                                    width = 100,
                                    height=30)
        self.move_to_theta_label_degree = CTkLabel(self.move_to_theta_frame, 
                                    text="°",
                                     font=("Roboto", 16))
        

        self.move_to_theta_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.move_to_theta_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.move_to_theta_label_degree.grid(row = 0, column = 2, padx = (5,10), pady = 10)
        

        self.move_to_theta_frame.place(relx = 0.55, rely = 0.6, anchor = "center")

        self.apply_move_to_button = CTkButton(self.move_to_frame,
                    text = "Apply",
                    font = ("Roboto", 20),
                    width = 75,
                    height = 50,
                    command = self.move_to)
        self.apply_move_to_button.place(relx = 0.85, rely = 0.6, anchor="center")



        ## Buttons for sequence test

        
        self.control_frame = CTkFrame(self,
                                        width = 340,
                                        height = 120)
        self.control_frame.place(relx = 0.8, rely = 0.47, anchor = "center")

        self.sequence_test_label = CTkLabel(self.control_frame,
                                         text="Sequence Test",
                                         font=("Roboto", 16),
                                         width = 320,
                                         corner_radius=10)
        self.sequence_test_label.place(relx = 0.5, rely = 0.15, anchor = "center")

        self.transparent_buttons = []
        self.control_buttons = [
            {"name": "Play", "icon": "play_icon.png", "command": self.playTestSequence},
            {"name": "Pause", "icon": "pause_icon.png", "command": self.pauseTestSequence},
            {"name": "Stop", "icon": "stop_icon.png", "command": self.stopTestSequence}
            ]
        
        for i in range(len(self.control_buttons)):
            element = self.control_buttons[i]
            
            image = Image.open("./img/"+element["icon"])
            icon = CTkImage(light_image = image,
                                dark_image=image,
                                size=(20,20))
                

            button = CTkButton(self.control_frame,
                                corner_radius= 10,
                                width = 20,
                                height = 20,
                                text=element["name"],
                                image=icon,
                                compound="top",
                                command = element["command"],
                                font=("Roboto", 16))
            self.transparent_buttons.append(button)
            button.place(relx = 0.2 + i*0.3, rely = 0.7, anchor = "center")
        

        ## Button for Photo test

        self.photo_test_button = CTkButton(self,
                    text = "Photo Test",
                    font = ("Roboto", 20),
                    width = 200,
                    height = 50,
                    command = lambda : send_command("picture"))

                
        self.photo_test_button.place(relx = 0.8, rely = 0.62, anchor = "center")

        ## Button for homing translation

        self.homing_button = CTkButton(self,
                    text = "Home motors",
                    font = ("Roboto", 20),
                    width = 200,
                    height = 50,
                    command = lambda : send_command("home"))

                
        self.homing_button.place(relx = 0.8, rely = 0.72, anchor = "center")
        
        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 1040,
                                        height = 150,
                                        font=("Roboto", 16),
                                        state = "disabled")
        self.logs_frame.place(relx = 0.5, rely = 0.88, anchor = "center")

        # Setting the default values
        self.reset_values()

    def reset_values(self):

        ## Position and Angle
        self.change_value("x_value", "0 mm", "disabled")

        self.change_value("theta_value", "0 °", "disabled")

        self.change_value("move_to_x_value", "0", "normal")
        self.change_value("move_to_theta_value", "0", "normal")


        self.logs_frame.delete("1.0", tk.END)
    
    def move_to(self):
        x = int(self.move_to_x_value.get("1.0", tk.END).strip())
        theta = int(self.move_to_theta_value.get("1.0", tk.END).strip())

        send_command("moveTo "+ str(x)+ " " + str(theta))



    def playTestSequence(self):

        if self.state == "STOPPED":
            self.state = "RUNNING"
            send_command("playTestSequence")

        if self.state == "PAUSED":
            self.state = "RUNNING"
            send_command("playTestSequence")
    def pauseTestSequence(self):
        if self.state == "RUNNING":
            self.state = "PAUSED"
            send_command("pauseTestSequence")

    def stopTestSequence(self):
        if self.state == "RUNNING" or self.state=="PAUSED":
            self.state = "STOPPED"
            send_command("stopTestSequence")

    def set_theme(self, theme):
        super().set_theme(theme)
        colors = themes[theme]

        self.movement_test_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.movement_test_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])

        self.translation_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])
        self.translation_label.configure(bg_color="transparent", fg_color=colors["sub_section_title"], text_color=colors["sub_section_title_text_color"])

        self.rotation_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])
        self.rotation_label.configure(bg_color="transparent", fg_color=colors["sub_section_title"], text_color=colors["sub_section_title_text_color"])


        self.translation_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])
        self.rotation_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])

        self.position_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.position_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])

        self.x_frame.configure(bg_color="transparent", fg_color=colors["panel_bg"])
        self.x_label.configure(bg_color="transparent", fg_color="transparent", text_color=colors["section_text_color"])
        self.x_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        self.theta_frame.configure(bg_color="transparent", fg_color=colors["panel_bg"])
        self.theta_label.configure(bg_color="transparent", fg_color="transparent", text_color=colors["section_text_color"])
        self.theta_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        self.move_to_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.move_to_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])

        self.move_to_x_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])
        self.move_to_x_label.configure(bg_color="transparent", fg_color="transparent", text_color=colors["section_text_color"])
        self.move_to_x_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.move_to_x_label_mm.configure(bg_color="transparent", fg_color="transparent", text_color=colors["section_text_color"])

        self.move_to_theta_frame.configure(bg_color="transparent", fg_color=colors["sub_section_bg"])
        self.move_to_theta_label.configure(bg_color="transparent", fg_color="transparent", text_color=colors["sub_section_text_color"])
        self.move_to_theta_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.move_to_theta_label_degree.configure(bg_color="transparent", fg_color="transparent", text_color=colors["sub_section_text_color"])

        self.apply_move_to_button.configure(bg_color="transparent", fg_color=colors["blue_button"], hover_color=colors["blue_button_hover"])

        self.control_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.sequence_test_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])

        self.photo_test_button.configure(bg_color="transparent", fg_color=colors["blue_button"], hover_color=colors["blue_button_hover"])
        self.homing_button.configure(bg_color="transparent", fg_color=colors["blue_button"], hover_color=colors["blue_button_hover"])

        self.logs_frame.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        for button in self.blue_buttons:
            button.configure(bg_color="transparent", fg_color=colors["blue_button"], hover_color=colors["blue_button_hover"])
        for button in self.red_buttons:
            button.configure(bg_color="transparent", fg_color=colors["red_button"], hover_color=colors["red_button_hover"])



        self.control_buttons = [
            {"name": "Play", "icon": "play_icon.png", "command": self.playTestSequence},
            {"name": "Pause", "icon": "pause_icon.png", "command": self.pauseTestSequence},
            {"name": "Stop", "icon": "stop_icon.png", "command": self.stopTestSequence}
            ]
        
        for i in range(len(self.control_buttons)):
            element = self.control_buttons[i]
            
            if (i < 2):
                image = Image.open("./img/"+element["icon"])
                image = color(image, colors["control_button"])
                icon = CTkImage(light_image = image,
                                    dark_image=image,
                                    size=(20,20))
                self.transparent_buttons[i].configure(image=icon)
    
            self.transparent_buttons[i].configure(fg_color = "transparent",hover_color = colors["section_button_hover"], text_color=colors["section_text_color"])