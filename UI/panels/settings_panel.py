from panels.panel import Panel
from customtkinter import *
import tkinter as tk

from communication import send_command

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
        
        self.translation_number_of_points_label = CTkLabel(self.translation_frame,
                                         text = "Number of points",
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
        self.translation_number_of_points_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.translation_speed_textbox = CTkTextbox(self.translation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)


        self.translation_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.translation_start_label.grid(row = 1, column = 0, padx = 10, pady = (50,10))
        self.translation_end_label.grid(row = 1, column = 2, padx = 10, pady = (50,10))
        self.translation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = (0,20))
        self.translation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = (0,20))

        self.translation_number_of_points_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.translation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.translation_number_of_points_textbox.grid(row = 4, column = 0, padx = 10, pady = (0,20))
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
        
        self.rotation_number_of_points_label = CTkLabel(self.rotation_frame,
                                         text = "Number of points",
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
        self.rotation_number_of_points_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)
        self.rotation_speed_textbox = CTkTextbox(self.rotation_frame,
                                    width = self.section_width/2*0.6,
                                    height = 20)

        self.rotation_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.rotation_start_label.grid(row = 1, column = 0, padx = 10, pady = (50,10))
        self.rotation_end_label.grid(row = 1, column = 2, padx = 10, pady = (50,10))
        self.rotation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = (0,20))
        self.rotation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = (0,20))

        self.rotation_number_of_points_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.rotation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.rotation_number_of_points_textbox.grid(row = 4, column = 0, padx = 10, pady = (0,20))
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
                                text="Apply configuration",
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400,
                                command = self.send_values)
        
        self.confirmation_button.place(relx = 0.25, rely = 0.9, anchor = "center")

        ## Reset Button

        self.reset_button = CTkButton(self,
                                text="Reset Configuration",
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400,
                                fg_color = "#8E0217",
                                hover_color="#582139",
                                command = lambda:self.reset_values(False)
                                )
        
        self.reset_button.place(relx = 0.25, rely = 0.8, anchor = "center")

        ## Estimation of time :
        self.estimated_time_frame = CTkFrame(self)
        self.estimated_time_frame.place(relx = 0.25, rely = 0.7, anchor = "center")

        self.estimated_time_label = CTkLabel(self.estimated_time_frame, 
                                    text="Estimated Time :",
                                     font=("Roboto", 15),
                                     )
        self.estimated_time_value = CTkTextbox(self.estimated_time_frame,
                                    width = 100,
                                    height=30,
                                    state = "disabled")

        self.estimated_time_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.estimated_time_value.grid(row = 0, column = 1, padx = (10,5), pady = 10)

        ## Panel of logs

        self.logs_frame = CTkTextbox(self,
                                        width = 575,
                                        height = 220,
                                        font=("Roboto", 16),
                                        state = "disabled"
                                        )
        self.logs_frame.place(relx = 0.7, rely = 0.8, anchor = "center")

        ## Setting the default values
        self.reset_values(True)
    
    def reset_values(self, initialization):
        # Translation
        self.change_value("translation_start_textbox", "0", "normal")
        self.change_value("translation_end_textbox", "20", "normal")
        self.change_value("translation_number_of_points_textbox", "3", "normal")
        self.change_value("translation_speed_textbox", "10", "normal")

        # Rotation

        self.change_value("rotation_start_textbox", "0", "normal")
        self.change_value("rotation_end_textbox", "20", "normal")
        self.change_value("rotation_number_of_points_textbox", "3", "normal")
        self.change_value("rotation_speed_textbox", "10", "normal")

        # Timings
        self.change_value("exposure_time_textbox", "1", "normal")
        self.change_value("saving_time_textbox", "1", "normal")
        self.change_value("margin_time_textbox", "1", "normal")

        # Estimated time
        self.change_value("estimated_time_value", "00:00:00", "disabled")

        # Logs
        if initialization:
            self.logs_frame.delete("1.0", tk.END)
        else:
            self.display_log("Resetted values to default")

    def send_values(self):
        # Translation
        translation_start = int(self.translation_start_textbox.get("1.0", tk.END).strip())
        send_command("change translation_starting_point " + str(translation_start))

        translation_end = float(self.translation_end_textbox.get("1.0", tk.END).strip())
        send_command("change translation_ending_point " + str(translation_end))

        translation_number_of_points = float(self.translation_number_of_points_textbox.get("1.0", tk.END).strip())
        send_command("change translation_number_of_points " + str(translation_number_of_points))

        translation_speed = float(self.translation_speed_textbox.get("1.0", tk.END).strip())
        send_command("change translation_speed " + str(translation_speed))

        # Rotation
        rotation_start = float(self.rotation_start_textbox.get("1.0", tk.END).strip())
        send_command("change rotation_starting_point " + str(rotation_start))

        rotation_end = float(self.rotation_end_textbox.get("1.0", tk.END).strip())
        send_command("change rotation_ending_point " + str(rotation_end))

        rotation_step = float(self.rotation_number_of_points_textbox.get("1.0", tk.END).strip())
        send_command("change rotation_number_of_points " + str(rotation_step))

        rotation_speed = float(self.rotation_speed_textbox.get("1.0", tk.END).strip())
        send_command("change rotation_speed " + str(rotation_speed))

        # Timings
        exposure_time = float(self.exposure_time_textbox.get("1.0", tk.END).strip())
        send_command("change exposure_time " + str(exposure_time))

        saving_time = float(self.saving_time_textbox.get("1.0", tk.END).strip())
        send_command("change saving_time " + str(saving_time))

        margin_time = float(self.margin_time_textbox.get("1.0", tk.END).strip())
        send_command("change margin_time " + str(margin_time))

        send_command("computeStep")

