from customtkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image
# from communication import *

def sendCommand(arg):
    pass

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

SIDEBAR_WIDTH = 100


class Panel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.width = (WINDOW_WIDTH-SIDEBAR_WIDTH)*0.97
        self.height = WINDOW_HEIGHT*0.97
        self.x, self.y = 0,0
        self.title = CTkLabel(self,width=int(self.width*0.9), text="",  fg_color="gray30", corner_radius=6, font=("Roboto", 20))
        self.title.place(relx =0.5, y = 50/2, anchor = "center")
        self.place(x=self.x,y=self.y)
        self.configure(width=self.width, height=self.height, corner_radius = 20, bg_color="transparent")


class ConnectionPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Connection")

        ## Box for the section "Connection Status"

        self.connection_status_frame = CTkFrame(self,
                                                width = 600,
                                                height = 340)
        self.connection_status_frame.place(relx = 0.69, rely = 0.32, anchor = "center")

        self.connection_status_label = CTkLabel(self.connection_status_frame,
                                         text = "Connection Status",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 580,
                                         corner_radius=10
                                         )
        
        self.connection_status_label.place(relx = 0.5, rely = 0.07, anchor = "center")
        self.indicator_radius = 10
        self.connection_status_indicator = CTkLabel(self.connection_status_frame,
                                         text = "",
                                         fg_color = "red",
                                         width = 2*self.indicator_radius,
                                         height = 2*self.indicator_radius,
                                         corner_radius=self.indicator_radius
                                         )
        self.connection_status_indicator.place(relx = 0.4, rely = 0.25, anchor = "center")
    
        self.connection_status_text = CTkLabel(self.connection_status_frame,
                                         text = "Disconnected",
                                         font = ("Roboto", 16)
                                         )
        self.connection_status_text.place(relx = 0.55, rely = 0.25, anchor = "center")

        
        self.connected_device_frame = CTkFrame(self.connection_status_frame)
        self.connected_device_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.connected_device_label = CTkLabel(self.connected_device_frame, 
                                    text="Connected Device :",
                                     font=("Roboto", 16),
                                     )
        self.connected_device_value = CTkTextbox(self.connected_device_frame,
                                    width = 300,
                                    height=30)

        self.connected_device_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.connected_device_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)



        self.firmware_version_frame = CTkFrame(self.connection_status_frame)

        self.firmware_version_frame = CTkFrame(self.connection_status_frame)
        self.firmware_version_frame.place(relx = 0.5, rely = 0.8, anchor = "center")

        self.firmware_version_label = CTkLabel(self.firmware_version_frame, 
                                    text="Firmware Version :",
                                     font=("Roboto", 16),
                                     )
        self.firmware_version_value = CTkTextbox(self.firmware_version_frame,
                                    width = 300,
                                    height=30)

        self.firmware_version_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.firmware_version_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.firmware_version_frame = CTkFrame(self.connection_status_frame)
       
        
        

        ## box for the section "Connection"

        self.connection_frame = CTkFrame(self)
        self.connection_label = CTkLabel(self.connection_frame,
                                          text = "Connection",
                                          font=("Roboto", 16),
                                          fg_color = "grey30",
                                          width = 400,
                                          corner_radius=10
                                          )
        self.connection_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        self.connection_frame.place(relx = 0.23, rely = 0.32, anchor = "center")
        
        
        self.available_ports = CTkComboBox(self.connection_frame, 
                                               values = ["COM1", "COM2", "COM3", "COM4"],
                                               )
        self.available_ports.grid(row = 1, column = 0, padx = (50,0), pady = 10)

        image = Image.open("./img/reset_icon.png")
        icon = CTkImage(light_image = image,
                        dark_image=image,
                        size=(20,20))
        

        self.search_connections_button = CTkButton(self.connection_frame,
                            width = 20,
                            height = 20,
                            corner_radius= 10,
                            text = "",
                            image=icon,
                            compound="top",
                            fg_color = "#2B2B2B",
                            hover_color="gray30")
        self.search_connections_button.grid(row = 1, column = 1, padx = (0,50), pady = 10)
        
        
        
        self.connect_button = CTkButton(self.connection_frame,
                                        text = "Connect",
                                        font = ("Roboto", 20),
                                        width = 250,
                                        height = 100)
        self.connect_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        
        self.disconnect_button = CTkButton(self.connection_frame,
                                        text = "Disconnect",
                                        font = ("Roboto", 20),
                                        width = 250,
                                        height = 100,
                                        fg_color = "#8E0217",
                                        hover_color="#582139")
        self.disconnect_button.grid(row = 3, column = 0,columnspan = 2, padx = 10, pady = 10)
       


        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 1040,
                                        height = 260,
                                        font=("Roboto", 16)
                                        )
        self.logs_frame.place(relx = 0.5, rely = 0.78, anchor = "center")


        

class TestPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Test")

        ## Box for the section "Test of the Movement"

        self.movement_test_frame = CTkFrame(self)
        self.movement_test_frame.place(relx = 0.35, rely = 0.42, anchor = "center")

        self.movement_test_label = CTkLabel(self.movement_test_frame,
                                            text = "Movement Test",
                                            font=("Roboto", 20),
                                            fg_color = "grey30",
                                            corner_radius=10)
        self.movement_test_label.grid(row = 0, column =0, columnspan = 2, sticky = "ew", padx = 10, pady = 10)

        self.translation_frame = CTkFrame(self.movement_test_frame)
        self.translation_label = CTkLabel(self.translation_frame,
                                         text = "Translation",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 300,
                                         corner_radius=10
                                         )
        
        self.rotation_frame = CTkFrame(self.movement_test_frame)
        self.rotation_label = CTkLabel(self.rotation_frame,
                                         text = "Rotation",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 300,
                                         corner_radius=10
                                         )

        self.translation_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        self.rotation_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

        self.translation_buttons = [[
            {"name": "+ 1 mm","command": lambda:sendCommand("move 1")},
            {"name": "+ 5 mm","command": lambda:sendCommand("move 5")},
            {"name": "+ 10 mm","command": lambda:sendCommand("move 10")},
        ],
        [
            {"name": "- 1 mm","command": lambda:sendCommand("move -1")},
            {"name": "- 5 mm","command": lambda:sendCommand("move -5")},
            {"name": "- 10 mm","command": lambda:sendCommand("move -10")},
        ]]

        self.rotation_buttons = [[
            {"name": "+ 1 °","command": lambda:sendCommand("turn 1")},
            {"name": "+ 5 °","command": lambda:sendCommand("turn 5")},
            {"name": "+ 10 °","command": lambda:sendCommand("turn 10")},
        ],
        [
            {"name": "- 1 °","command": lambda:sendCommand("turn -1")},
            {"name": "- 5 °","command": lambda:sendCommand("turn -5")},
            {"name": "- 10 °","command": lambda:sendCommand("turn -10")}
        ]]
                      
        for i in range(len(self.translation_buttons)):
            for j in range(len(self.translation_buttons[i])):
                if i == 0:
                    color = "#1F6AA5"
                    hover_color = "#144870"
                else:
                    color = "#8E0217"
                    hover_color="#582139"

                button = CTkButton(self.translation_frame,
                    text = self.translation_buttons[i][j]["name"],
                    height = 100,
                    width = 100,
                    command = self.translation_buttons[i][j]["command"],
                    fg_color= color,
                    hover_color= hover_color)
                
                button.grid(row=j+1, column=i,padx = 10, pady = 10)

        for i in range(len(self.rotation_buttons)):
            for j in range(len(self.rotation_buttons[i])):
                if i == 0:
                    color = "#1F6AA5"
                    hover_color = "#144870"
                else:
                    color = "#8E0217"
                    hover_color="#582139"

                button = CTkButton(self.rotation_frame,
                    text = self.rotation_buttons[i][j]["name"],
                    height = 100,
                    width = 100,
                    command = self.rotation_buttons[i][j]["command"],
                    fg_color= color,
                    hover_color= hover_color)
                
                button.grid(row=j+1, column=i,padx = 10, pady = 10)


        self.translation_frame.grid(row = 1, rowspan= 2, column = 0, padx = 10, pady = 10)
        self.rotation_frame.grid(row = 1,rowspan = 2,column = 1, padx = 10, pady = 10)

        ## Button for sequence test

        self.sequence_test_button = CTkButton(self,
                    text = "Sequence Test",
                    font = ("Roboto", 20),
                    width = 300,
                    height = 100)

                
        self.sequence_test_button.place(relx = 0.8, rely = 0.4, anchor = "center")

        ## Button for connection test

        self.connection_test_button = CTkButton(self,
                    text = "Connection Test",
                    font = ("Roboto", 20),
                    width = 300,
                    height = 100)

                
        self.connection_test_button.place(relx = 0.8, rely = 0.6, anchor = "center")

        ## Button for Photo test

        self.photo_test_button = CTkButton(self,
                    text = "Photo Test",
                    font = ("Roboto", 20),
                    width = 300,
                    height = 100)

                
        self.photo_test_button.place(relx = 0.8, rely = 0.2, anchor = "center")


        
        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 1040,
                                        height = 150,
                                        font=("Roboto", 16)
                                        )
        self.logs_frame.place(relx = 0.5, rely = 0.88, anchor = "center")







class SettingsPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Capture Settings")

        self.section_width = 300
        self.section_height = 300


        ## Box that contains a section "Translation", a section "Rotation", and a section "Timing"
        self.settings_frame = CTkFrame(self,
                                            fg_color = "#333333"
                                            )
        self.settings_frame.place(relx=0.5, rely=0.35, anchor = "center")
    

        ## Box of the section "Translation"
        self.translation_frame = CTkFrame(self.settings_frame,
                                            fg_color = "#2B2B2B",
                                            bg_color = "#333333",
                                            corner_radius=10,
                                            )
        self.translation_frame.grid(row =0, column = 0, padx = 10, sticky = "ns")

        self.translation_label = CTkLabel(self.translation_frame,
                                         text = "Translation",
                                         font=("Roboto", 20),
                                         fg_color = "grey30",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.translation_start_label = CTkLabel(self.translation_frame,
                                         text = "Starting Point (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_end_label = CTkLabel(self.translation_frame,
                                         text = "Ending Point (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.translation_step_label = CTkLabel(self.translation_frame,
                                         text = "Step (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_speed_label = CTkLabel(self.translation_frame,
                                         text = "Speed (%)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )

        self.translation_start_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.translation_end_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.translation_step_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.translation_speed_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
       
        ## Test for value interactions
        self.translation_start_textbox.delete("1.0", tk.END)
        self.translation_start_textbox.insert("1.0", "0")

        print(self.translation_start_textbox.get("1.0", tk.END))

        #///////////////////////

       

        self.translation_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.translation_start_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.translation_end_label.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.translation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = (0,20))
        self.translation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = (0,20))

        self.translation_step_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.translation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.translation_step_textbox.grid(row = 4, column = 0, padx = 10, pady = (0,20))
        self.translation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = (0,20))
        

        ## Box of the section "Rotation"

        self.rotation_frame = CTkFrame(self.settings_frame,
                                            fg_color = "#2B2B2B",
                                            bg_color = "#333333",
                                            corner_radius=10
                                            )

        self.rotation_frame.grid(row =0, column = 1, padx = 10, sticky = "ns")

        self.rotation_label = CTkLabel(self.rotation_frame,
                                         text = "Rotation",
                                         font=("Roboto", 20),
                                         fg_color = "grey30",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.rotation_start_label = CTkLabel(self.rotation_frame,
                                         text = "Starting Point (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.rotation_end_label = CTkLabel(self.rotation_frame,
                                         text = "Ending Point (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.rotation_step_label = CTkLabel(self.rotation_frame,
                                         text = "Step (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.rotation_speed_label = CTkLabel(self.rotation_frame,
                                         text = "Speed (%)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )

        self.rotation_start_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.rotation_end_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.rotation_step_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.rotation_speed_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)

        self.rotation_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.rotation_start_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.rotation_end_label.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.rotation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = (0,20))
        self.rotation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = (0,20))

        self.rotation_step_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.rotation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.rotation_step_textbox.grid(row = 4, column = 0, padx = 10, pady = (0,20))
        self.rotation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = (0,20))

    
        ## Box of the section "Timings"
        self.timing_frame = CTkFrame(self.settings_frame,
                                            fg_color = "#2B2B2B",
                                            bg_color = "#333333",
                                            corner_radius=10,
                                            )

        self.timing_frame.grid(row =0, column = 2, padx = 10, sticky = "ns")

        self.timing_label = CTkLabel(self.timing_frame,
                                         text = "Timings",
                                         font=("Roboto", 20),
                                         fg_color = "grey30",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.exposure_time_label = CTkLabel(self.timing_frame,
                                         text = "Exposure Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.saving_time_label = CTkLabel(self.timing_frame,
                                         text = "Saving Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.margin_time_label = CTkLabel(self.timing_frame,
                                         text = "Margin Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey20",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.exposure_time_textbox = CTkTextbox(self.timing_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.saving_time_textbox = CTkTextbox(self.timing_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.margin_time_textbox = CTkTextbox(self.timing_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)

        self.timing_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

        self.exposure_time_label.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.exposure_time_textbox.grid(row = 2, column = 1, padx = 10, pady = (0,20))

        self.saving_time_label.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.saving_time_textbox.grid(row = 4, column = 1, padx = 10, pady = (0,20))

        self.margin_time_label.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.margin_time_textbox.grid(row = 6, column = 1, padx = 10, pady = (0,20))

        ## Validation Button

        self.confirmation_button = CTkButton(self,
                                text="Send Configuration",
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400)
        
        self.confirmation_button.place(relx = 0.25, rely = 0.85, anchor = "center")

        ## Reset Button

        self.reset_button = CTkButton(self,
                                text="Reset Configuration",
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400,
                                fg_color = "#8E0217",
                                hover_color="#582139"
                                )
        
        self.reset_button.place(relx = 0.25, rely = 0.75, anchor = "center")


        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 575,
                                        height = 220,
                                        font=("Roboto", 16)
                                        )
        self.logs_frame.place(relx = 0.7, rely = 0.8, anchor = "center")


class CapturePanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Capture")

        
        ## Box for the section "Control of the capture"
        self.control_frame = CTkFrame(self,
                                        width = 400,
                                        height = 200,
                                        )
        self.control_frame.place(relx = 0.24, rely = 0.22, anchor = "center")

        self.control_label = CTkLabel(self.control_frame,
                                         text="Control",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 380,
                                         corner_radius=10
                                         )
        self.control_label.place(relx = 0.5, rely = 0.1, anchor = "center")

        self.control_buttons = [
            {"name": "Play", "icon": "play_icon.png", "command": sendCommand("play")},
            {"name": "Pause", "icon": "pause_icon.png", "command": sendCommand("pause")},
            {"name": "Stop", "icon": "stop_icon.png", "command": sendCommand("stop")}
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
                                font=("Roboto", 16),
                                text_color="#D9D9D9",
                                fg_color = "#2B2B2B",
                                hover_color="gray30")

            button.place(relx = 0.2 + i*0.3, rely = 0.6, anchor = "center")
        
        ## Box for the section "Position and Angle"
        self.position_frame = CTkFrame(self,
                                        width = 400,
                                        height = 200,
                                        )
        self.position_frame.place(relx = 0.24, rely = 0.52, anchor = "center")

        self.position_label = CTkLabel(self.position_frame,
                                         text="Position and Angle",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 380,
                                         corner_radius=10
                                         )
        self.position_label.place(relx = 0.5, rely = 0.1, anchor = "center")

        self.x_frame = CTkFrame(self.position_frame)
        self.x_label = CTkLabel(self.x_frame, 
                                    text="x :",
                                     font=("Roboto", 16),
                                     )
        self.x_value = CTkTextbox(self.x_frame,
                                    width = 100,
                                    height=30)
        self.x_label_mm = CTkLabel(self.x_frame, 
                                    text="mm",
                                     font=("Roboto", 16),
                                     )

        self.x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.x_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.x_label_mm.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.x_frame.place(relx = 0.5, rely = 0.35, anchor = "center")

        self.theta_frame = CTkFrame(self.position_frame)
        self.theta_label = CTkLabel(self.theta_frame, 
                                    text="Theta :",
                                     font=("Roboto", 16),
                                     )
        self.theta_value = CTkTextbox(self.theta_frame,
                                    width = 100,
                                    height=30)
        self.theta_label_mm = CTkLabel(self.theta_frame, 
                                    text="°",
                                     font=("Roboto", 16),
                                     )

        self.theta_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.theta_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.theta_label_mm.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.theta_frame.place(relx = 0.5, rely = 0.7, anchor = "center")



        ## Box for the section "Status of the Capture"
        self.status_frame = CTkFrame(self,
                                        width = 550,
                                        height = 415,
                                
        )
        self.status_frame.place(relx = 0.69, rely = 0.37, anchor = "center")

        self.status_label = CTkLabel(self.status_frame,
                                         text="Capture Status",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 530,
                                         corner_radius=10
                                         )

        self.status_label.place(relx = 0.5, rely = 0.05, anchor = "center")

        
        self.progress_bar = CTkProgressBar(self.status_frame,
                                            height = 20,
                                            width =400)
        self.progress_percentage = CTkLabel(self.status_frame,
                                                font = ("Roboto", 15),
                                                text = "50%")
        self.progress_bar.place(relx = 0.45, rely = 0.2, anchor = "center")
        self.progress_percentage.place(relx = 0.9, rely = 0.2, anchor = "center")


        self.time_frame = CTkFrame(self.status_frame)
        self.time_frame.place(relx = 0.25, rely = 0.35, anchor = "center")

        self.time_label = CTkLabel(self.time_frame, 
                                    text="Capture Time :",
                                     font=("Roboto", 15),
                                     )
        self.time_value = CTkTextbox(self.time_frame,
                                    width = 100,
                                    height=30)

        self.time_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.time_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.estimated_time_frame = CTkFrame(self.status_frame)
        self.estimated_time_frame.place(relx = 0.75, rely = 0.35, anchor = "center")

        self.estimated_time_label = CTkLabel(self.estimated_time_frame, 
                                    text="Estimated Time\nLeft :",
                                     font=("Roboto", 15),
                                     )
        self.estimated_time_value = CTkTextbox(self.estimated_time_frame,
                                    width = 100,
                                    height=30)

        self.estimated_time_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.estimated_time_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        self.nb_pictures_frame = CTkFrame(self.status_frame)
        self.nb_pictures_frame.place(relx = 0.5, rely = 0.55, anchor = "center")

        self.nb_pictures_label = CTkLabel(self.nb_pictures_frame, 
                                    text="Total Pictures Taken :",
                                     font=("Roboto", 15),
                                     )
        self.nb_pictures_value = CTkTextbox(self.nb_pictures_frame,
                                    width = 100,
                                    height=30)
        self.total_nb_pictures_label = CTkLabel(self.nb_pictures_frame, 
                                    text="/ 100",
                                     font=("Roboto", 15),
                                     )

        self.nb_pictures_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.nb_pictures_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_nb_pictures_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.nb_pictures_angle_frame = CTkFrame(self.status_frame)
        self.nb_pictures_angle_frame.place(relx = 0.5, rely = 0.7, anchor = "center")

        self.nb_pictures_angle_label = CTkLabel(self.nb_pictures_angle_frame, 
                                    text="Pictures taken for this angle :",
                                     font=("Roboto", 15),
                                     )
        self.nb_pictures_angle_value = CTkTextbox(self.nb_pictures_angle_frame,
                                    width = 100,
                                    height=30)
        self.total_nb_pictures_angle_label = CTkLabel(self.nb_pictures_angle_frame, 
                                    text="/ 100",
                                     font=("Roboto", 15),
                                     )

        self.nb_pictures_angle_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.nb_pictures_angle_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_nb_pictures_angle_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        self.explored_angles_frame = CTkFrame(self.status_frame)
        self.explored_angles_frame.place(relx = 0.5, rely = 0.85, anchor = "center")

        self.explored_angles_label = CTkLabel(self.explored_angles_frame, 
                                    text="Number of angles completed :",
                                     font=("Roboto", 15),
                                     )
        self.explored_angles_value = CTkTextbox(self.explored_angles_frame,
                                    width = 100,
                                    height=30)
        self.total_explored_angles_label = CTkLabel(self.explored_angles_frame, 
                                    text="/ 100",
                                     font=("Roboto", 15),
                                     )

        self.explored_angles_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.explored_angles_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)
        self.total_explored_angles_label.grid(row = 0, column = 2, padx =(5,10),pady = 10)

        # Box for the logs

        self.logs_frame = CTkTextbox(self,
                                    width = 990,
                                    height = 200)
        self.logs_frame.place(relx = 0.5, rely = 0.82, anchor = "center")


        


class PanelContainer(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.width = WINDOW_WIDTH - SIDEBAR_WIDTH
        self.height = WINDOW_HEIGHT
        

        self.configure(width = self.width, height = self.height , corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.state = "Settings"
        


        self.panels = {"Connection": ConnectionPanel(self), "Test": TestPanel(self), "Settings": SettingsPanel(self), "Capture": CapturePanel(self)}
        for panel in self.panels.values():
            panel.place(relx = -1, rely = 0.5, anchor = "center")
            panel.x, panel.y = -self.width, 0
        
        self.panels["Settings"].place(relx = 0.5, rely = 0.5, anchor = "center")
        self.panels["Settings"].x = 0
        
        
        
        
        
    def setPanel(self, panel_name):
        if panel_name==self.state:
            return 0

        current_panel = self.panels[self.state]
        new_panel = self.panels[panel_name]
        current_panel.place(relx = -1)
        new_panel.place(relx = 0.5)

        self.state = panel_name

        return 1



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



class SettingsButton(CTkButton):
    def __init__(self, master):
        super().__init__(master)

        self.width = 100
        self.height = 100
        image = Image.open("./img/settings_icon.png")
        icon = CTkImage(light_image = image,dark_image=image, size = (40,40))
        self.configure( self,  
                        image=icon, 
                        width=100,
                        height=100,
                        corner_radius= 40,
                        text="General Settings",
                        compound="top",
                        bg_color = "#333333",
                        fg_color = "#2B2B2B",
                        hover_color="gray30",
                        font=("Roboto", 16),
                        text_color="#D9D9D9",
                        command = self.open_settings)
        
    def open_settings(self):
            self.settings_window = CTkToplevel(self.master)
            self.settings_window.geometry("600x400")
            self.settings_window.title("Settings")


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Endoscope Application")
        self.geometry(str(WINDOW_WIDTH)+ "x"+ str(WINDOW_HEIGHT))
        self.grid_columnconfigure(1, weight=1)
        self.resizable(False, False)

        print(self.winfo_screenwidth(), self.winfo_width())
       
        self.grid_rowconfigure(0, weight=1)

        self.panel_container = PanelContainer(self)
        self.panel_container.place(x = 100, y = 0)


        self.sidebar = Sidebar(self, self.panel_container)
        self.sidebar.place(x = 0, y = 0)

        # self.settings_button = SettingsButton(self)
        # self.settings_button.place(relx=0.9, rely=0.9, anchor = "center")
        

app = App()
app.mainloop()