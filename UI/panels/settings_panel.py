from panels.panel import Panel
from customtkinter import *
import tkinter as tk
from const import *
from languages import *

from themes import themes

from communication import send_command

class SettingsPanel(Panel):
    def __init__(self, master):
        super().__init__(master)

        self.section_width = 300
        self.section_height = 400

        self.modes = ["Translation First", "Rotation First"]
        self.current_mode = self.modes[0]


        ## Box that contains a section "Translation", a section "Rotation", and a section "Timing"
        self.settings_frame = CTkFrame(self)
        self.settings_frame.configure(width = WINDOW_WIDTH,
                                      height= self.section_height)
        self.settings_frame.place(relx=0.5, rely=0.35, anchor = "center")
    

        ## Box of the section "Translation"
        self.translation_frame = CTkFrame(self.settings_frame,
                                            corner_radius=10,
                                            )
        self.translation_frame.place(relx=0.23, rely=0.38, anchor= "center")

        self.translation_label = CTkLabel(self.translation_frame,
                                         font=("Roboto", 20),
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width)
        
    
        self.translation_start_label = CTkLabel(self.translation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_end_label = CTkLabel(self.translation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.translation_number_of_points_label = CTkLabel(self.translation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_speed_label = CTkLabel(self.translation_frame,
                                         font=("Roboto", 16),
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
        self.translation_start_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.translation_end_label.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.translation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.translation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.translation_number_of_points_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.translation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.translation_number_of_points_textbox.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.translation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = 10)
        

        ## Box of the section "Rotation"

        self.rotation_frame = CTkFrame(self.settings_frame,
                                            corner_radius=10)

        self.rotation_frame.place(relx=0.53, rely=0.38, anchor= "center")

        self.rotation_label = CTkLabel(self.rotation_frame,
                                         font=("Roboto", 20),
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width)
        
    
        self.rotation_start_label = CTkLabel(self.rotation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
        self.rotation_end_label = CTkLabel(self.rotation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
        
        self.rotation_number_of_points_label = CTkLabel(self.rotation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
        self.rotation_speed_label = CTkLabel(self.rotation_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)

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
        self.rotation_start_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.rotation_end_label.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.rotation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.rotation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.rotation_number_of_points_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.rotation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.rotation_number_of_points_textbox.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.rotation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = 10)

    
        ## Box of the section "Timings"
        self.timing_frame = CTkFrame(self.settings_frame,
                                            corner_radius=10)

        self.timing_frame.place(relx=0.8, rely=0.5  , anchor= "center")

        self.timing_label = CTkLabel(self.timing_frame,
                                         font=("Roboto", 20),
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width)
        
    
        self.exposure_time_label = CTkLabel(self.timing_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
        self.saving_time_label = CTkLabel(self.timing_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
        
        self.margin_time_label = CTkLabel(self.timing_frame,
                                         font=("Roboto", 16),
                                         width = self.section_width/2*0.8,
                                         corner_radius=10)
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

        ## Box of the section "Mode"
        self.mode_frame = CTkFrame(self.settings_frame,
                                            corner_radius=10,
                                            width = 750,
                                            height = 85)

        self.mode_frame.place(relx=0.375, rely=0.87  , anchor= "center")

        self.mode_label = CTkLabel(self.mode_frame,
                                         font=("Roboto", 20),
                                         corner_radius=10,
                                         width = 730)
        self.mode_label.place(relx=0.5, rely = 0.3, anchor= "center")
        
        self.mode_combobox = CTkComboBox(self.mode_frame, width = 300)
        self.mode_combobox.place(relx = 0.5, rely = 0.76, anchor = "center")

        ## Validation Button

        self.confirmation_button = CTkButton(self,
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400,
                                command = self.send_values)
        
        self.confirmation_button.place(relx = 0.25, rely = 0.9, anchor = "center")

        ## Reset Button

        self.reset_button = CTkButton(self,
                                font = ("Roboto", 20),
                                height = 50,
                                width = 400,
                                command = lambda:self.reset_values(False)
                                )
        
        self.reset_button.place(relx = 0.25, rely = 0.8, anchor = "center")

        ## Estimation of time :
        self.estimated_time_frame = CTkFrame(self,
                                             corner_radius=10)
        self.estimated_time_frame.place(relx = 0.25, rely = 0.7, anchor = "center")

        self.estimated_time_label = CTkLabel(self.estimated_time_frame,
                                     font=("Roboto", 15))
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
                                        state = "disabled")
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

        # Mode
        self.mode_combobox.set(self.modes[0])

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

        # Mode
        mode = self.modes.index(self.mode_combobox.get())
        print(mode)
        send_command("change mode " + str(mode))

        send_command("computeStep")

    def set_theme(self, theme):
        super().set_theme(theme)

        colors = themes[theme]

        # Frame Settings
        self.settings_frame.configure(bg_color="transparent", fg_color=colors["panel_bg"])

        # Translation Section
        self.translation_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.translation_label.configure(text_color=colors["section_title_text_color"], fg_color=colors["section_title"], bg_color="transparent")
        self.translation_start_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.translation_end_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.translation_number_of_points_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.translation_speed_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")

        self.translation_start_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.translation_end_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.translation_number_of_points_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.translation_speed_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        # Rotation Section
        self.rotation_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.rotation_label.configure(text_color=colors["section_title_text_color"], fg_color=colors["section_title"], bg_color="transparent")
        self.rotation_start_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.rotation_end_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.rotation_number_of_points_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.rotation_speed_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")

        self.rotation_start_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.rotation_end_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.rotation_number_of_points_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.rotation_speed_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        # Timings Section
        self.timing_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.timing_label.configure(text_color=colors["section_title_text_color"], fg_color=colors["section_title"], bg_color="transparent")
        self.exposure_time_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.saving_time_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")
        self.margin_time_label.configure(text_color=colors["sub_section_title_text_color"], fg_color=colors["sub_section_title"], bg_color="transparent")

        self.exposure_time_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.saving_time_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])
        self.margin_time_textbox.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        # Mode section

        self.mode_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.mode_label.configure(text_color=colors["section_title_text_color"], fg_color=colors["section_title"], bg_color="transparent")
        self.mode_combobox.configure(
                                        fg_color = colors["combobox_fg"],
                                        text_color = colors["combobox_text_color"],
                                        border_color = colors["combobox_border"],
                                        button_color = colors["combobox_button"],
                                        dropdown_fg_color= colors["combobox_dropdown_fg"],
                                        
                                        dropdown_text_color= colors["combobox_dropdown_text_color"],
                                        
                                        dropdown_hover_color = colors["combobox_dropdown_hover"],
                                       
                                        button_hover_color = colors["combobox_button_hover"]
        )
        # Confirmation Button
        self.confirmation_button.configure(fg_color=colors["blue_button"], bg_color="transparent", hover_color=colors["blue_button_hover"])

        # Reset Button
        self.reset_button.configure(fg_color = colors["red_button"], bg_color= "transparent", hover_color=colors["red_button_hover"])

        # Estimated Time Section
        self.estimated_time_frame.configure(bg_color="transparent", fg_color=colors["section_bg"])
        self.estimated_time_label.configure(text_color=colors["section_text_color"], fg_color="transparent", bg_color="transparent")
        self.estimated_time_value.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

        # Logs Panel
        self.logs_frame.configure(bg_color="transparent", fg_color=colors["textbox_bg"], text_color=colors["textbox_text_color"])

    def set_language(self, name):

        language = languages[name]
        self.title.configure(text=language["Capture Settings"])

        self.translation_label.configure(text=language["Translation"])
        self.translation_start_label.configure(text=language["Starting Point"] + " (mm)")
        self.translation_end_label.configure(text=language["Ending Point"] + " (mm)")
        self.translation_number_of_points_label.configure(text=language["Number of Points"])
        self.translation_speed_label.configure(text=language["Translation Speed"] + " (%)")

        self.rotation_label.configure(text=language["Rotation"])
        self.rotation_start_label.configure(text=language["Starting Point"] + " (°)")
        self.rotation_end_label.configure(text=language["Ending Point"] + " (°)")
        self.rotation_number_of_points_label.configure(text=language["Number of Points"])
        self.rotation_speed_label.configure(text=language["Rotation Speed"] + " (%)")

        self.timing_label.configure(text=language["Timings"])
        self.exposure_time_label.configure(text=language["Exposure Time"] +" (s)")
        self.saving_time_label.configure(text=language["Saving Time"]+ " (s)")
        self.margin_time_label.configure(text=language["Margin Time"] + " (s)")

        self.mode_label.configure(text = language["Mode"])
        self.modes = [language["Translation First"], language["Rotation First"]]
        self.mode_combobox.configure(values=self.modes)
        self.mode_combobox.set(self.modes[0])

        self.confirmation_button.configure(text=language["Apply Configuration"])
        self.reset_button.configure(text=language["Reset values to default"])

        self.estimated_time_label.configure(text=language["Estimated Time"] + " :")




