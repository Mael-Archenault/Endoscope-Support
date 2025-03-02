from panels.panel import Panel
from customtkinter import *
from PIL import Image
from communication import initialize_connection, get_available_ports, close_connection, send_command
from const import *
from color import color

import tkinter as tk
from languages import *

from themes import themes


class ConnectionPanel(Panel):
    def __init__(self, master):
        super().__init__(master)

        self.connnection_status = ["Disconnected", "Connected"]
        self.connected = False

        ## Box for the section "Connection Status"

        self.connection_status_frame = CTkFrame(self,
                                                width = 600,
                                                height = 340,
                                                corner_radius = 10)
        self.connection_status_frame.place(relx = 0.69, rely = 0.32, anchor = "center")

        self.connection_status_label = CTkLabel(self.connection_status_frame,
                                         font=("Roboto", 16),
                                         width = 580,
                                         corner_radius=10)
        
        self.connection_status_label.place(relx = 0.5, rely = 0.07, anchor = "center")
        self.indicator_radius = 10
        self.connection_status_indicator = CTkLabel(self.connection_status_frame,
                                         text = "",
                                         fg_color = "red",
                                         width = 2*self.indicator_radius,
                                         height = 2*self.indicator_radius,
                                         corner_radius=self.indicator_radius,
                                         )
        self.connection_status_indicator.place(relx = 0.4, rely = 0.25, anchor = "center")
    
        self.connection_status_text = CTkLabel(self.connection_status_frame,
                                         font = ("Roboto", 16))
        
        self.connection_status_text.place(relx = 0.55, rely = 0.25, anchor = "center")

        
        self.connected_device_frame = CTkFrame(self.connection_status_frame)
        self.connected_device_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.connected_device_label = CTkLabel(self.connected_device_frame,
                                     font=("Roboto", 16))
        self.connected_device_value = CTkTextbox(self.connected_device_frame,
                                    width = 300,
                                    height=30,
                                    state = "disabled")

        self.connected_device_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.connected_device_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)



        self.firmware_version_frame = CTkFrame(self.connection_status_frame)

        self.firmware_version_frame.place(relx = 0.5, rely = 0.8, anchor = "center")

        self.firmware_version_label = CTkLabel(self.firmware_version_frame,
                                    font=("Roboto", 16))
        self.firmware_version_value = CTkTextbox(self.firmware_version_frame,
                                    width = 300,
                                    height=30,
                                    state = "disabled")

        self.firmware_version_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.firmware_version_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        ## box for the section "Connection"

        self.connection_frame = CTkFrame(self)
        self.connection_label = CTkLabel(self.connection_frame,
                                          font=("Roboto", 16),
                                          width = 400,
                                          corner_radius=10)
        self.connection_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        self.connection_frame.place(relx = 0.23, rely = 0.32, anchor = "center")
        
        
        self.available_ports = CTkComboBox(self.connection_frame, 
                                               values = get_available_ports())
        self.available_ports.grid(row = 1, column = 0, padx = (50,0), pady = 10)

        image = Image.open("./img/reset_icon.png")
        icon = CTkImage(light_image = image,
                        dark_image=image,
                        size=(20,20))
        

        self.refresh_ports_button = CTkButton(self.connection_frame,
                            width = 20,
                            height = 20,
                            corner_radius= 10,
                            text = "",
                            image=icon,
                            compound="top",
                            command= self.refresh_ports)
        self.refresh_ports_button.grid(row = 1, column = 1, padx = (0,50), pady = 10)
        
        
        
        self.connect_button = CTkButton(self.connection_frame,
                                        font = ("Roboto", 20),
                                        width = 250,
                                        height = 100,
                                        command = self.connect)
        self.connect_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        
        self.disconnect_button = CTkButton(self.connection_frame,
                                        font = ("Roboto", 20),
                                        width = 250,
                                        height = 100,
                                        command = self.disconnect)
        self.disconnect_button.grid(row = 3, column = 0,columnspan = 2, padx = 10, pady = 10)
       


        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 1040,
                                        height = 260,
                                        font=("Roboto", 16),
                                        state="disabled")
        self.logs_frame.place(relx = 0.5, rely = 0.78, anchor = "center")

        # Setting the default values
        self.reset_values()

    
    def reset_values(self):
        self.connection_status_indicator.configure(fg_color = "red")

        self.connected_device_value.configure(state = "normal")
        self.connected_device_value.delete(1.0, tk.END)
        self.connected_device_value.configure(state = "disabled")
        
        self.firmware_version_value.configure(state = "normal")
        self.firmware_version_value.delete(1.0, tk.END)
        self.firmware_version_value.configure(state = "disabled")

        self.logs_frame.delete(1.0, tk.END)
        
        available_ports = get_available_ports()
        if len(available_ports)>0:
            self.available_ports.set(available_ports[0])
        else:
            self.available_ports.set("")
        self.available_ports.configure(values = available_ports)

    def refresh_ports(self):
        available_ports = get_available_ports()
        if len(available_ports)>0:
            self.available_ports.set(available_ports[0])
        else:
            self.available_ports.set("")
            
        self.available_ports.configure(values = available_ports)
        self.display_log("Refreshed available COM ports : " + str(available_ports))
    def connect(self):
        com_port = self.available_ports.get().split('(')[-1][:-1] # a bit ugly, but works
        device = self.available_ports.get().split('(')[0]

        res, err = initialize_connection(com_port)

        if (res==-1):
            self.display_log(err)
        
        else:
            self.connection_status_indicator.configure(fg_color = "green")
            self.connection_status_text.configure(text = self.connection_status[1])
            self.connected = True

            self.connected_device_value.configure(state = "normal")
            self.connected_device_value.delete(1.0, tk.END)
            self.connected_device_value.insert(tk.END, device)
            self.connected_device_value.configure(state = "disabled")

            send_command("getFirmware")
            self.display_log("Connected to port : "+com_port)
    def disconnect(self):
        res, err = close_connection()
        if res == -1:
            self.display_log(err)
        else:
            self.connection_status_indicator.configure(fg_color = "red")
            self.connection_status_text.configure(text = self.connection_status[0])
            self.connected = False
            self.reset_values()
            self.display_log("Disconnected")

    def set_theme(self, theme):
        super().set_theme(theme)
        colors = themes[theme]
        self.connection_status_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.connection_status_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])
        self.connection_status_indicator.configure(bg_color="transparent", fg_color="red", text_color=colors["section_text_color"])
        self.connection_status_text.configure(text_color=colors["section_title_text_color"])
        self.connected_device_frame.configure(bg_color="transparent", fg_color=colors["panel_bg"])
        self.connected_device_label.configure(text_color=colors["section_text_color"])
        self.connected_device_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.firmware_version_frame.configure(bg_color="transparent", fg_color=colors["panel_bg"])
        self.firmware_version_label.configure(text_color=colors["section_text_color"])
        self.firmware_version_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.connection_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.connection_label.configure(bg_color="transparent", fg_color=colors["section_title"], text_color=colors["section_title_text_color"])
        
        self.refresh_ports_button.configure(bg_color="transparent", fg_color=colors["section_bg"], hover_color=colors["section_button_hover"])
        self.connect_button.configure(bg_color="transparent", fg_color=colors["blue_button"], hover_color=colors["blue_button_hover"])
        self.disconnect_button.configure(bg_color="transparent", fg_color=colors["red_button"], hover_color=colors["red_button_hover"])
        self.logs_frame.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        image = Image.open("./img/reset_icon.png")
        image = color(image, colors["refresh_button"])
        icon = CTkImage(light_image = image,
                        dark_image=image,
                        size=(20,20))
        self.refresh_ports_button.configure(image=icon)

        self.available_ports.configure(
                                        fg_color = colors["combobox_fg"],
                                        text_color = colors["combobox_text_color"],
                                        border_color = colors["combobox_border"],
                                        button_color = colors["combobox_button"],
                                        dropdown_fg_color= colors["combobox_dropdown_fg"],
                                        
                                        dropdown_text_color= colors["combobox_dropdown_text_color"],
                                        
                                        dropdown_hover_color = colors["combobox_dropdown_hover"],
                                       
                                        button_hover_color = colors["combobox_button_hover"])

    def set_language(self, name):
        language = languages[name]
        self.title.configure(text = language["Connection"])
        self.connection_label.configure(text=language["Connection"])
        self.connection_status_label.configure(text=language["Connection Status"])
        self.connected_device_label.configure(text=language["Connected Device"] + " :")
        self.firmware_version_label.configure(text=language["Firmware Version"] + " :")
        self.connect_button.configure(text=language["Connect"])
        self.disconnect_button.configure(text=language["Disconnect"])

        self.connection_status = [language["Disconnected"], language["Connected"]]
        if self.connected:
            self.connection_status_text.configure(text = self.connection_status[1])
        else:
            self.connection_status_text.configure(text = self.connection_status[0])
        


        
        
