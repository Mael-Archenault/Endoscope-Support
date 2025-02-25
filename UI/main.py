from customtkinter import *
import tkinter as tk
from PIL import Image
# from communication import *

def sendCommand():
    pass

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

SIDEBAR_WIDTH = 100


class Panel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.width = WINDOW_WIDTH-SIDEBAR_WIDTH
        self.height = WINDOW_HEIGHT
        self.x, self.y = 0,0
        self.title = CTkLabel(self,width=int(self.width*0.9), text="",  fg_color="gray30", corner_radius=6, font=("Roboto", 20))
        self.title.place(relx =0.5, y = 50/2, anchor = "center")
        self.place(x=self.x,y=self.y)
        self.configure(width=self.width, height=self.height, corner_radius = 20, bg_color="transparent")


class MovePanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Move")



class TestPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Test")

        
        self.test_frame = CTkFrame(self)
        self.test_frame.place(x =150,y =100)

        self.translation_frame = CTkFrame(self.test_frame)
        self.translation_label = CTkLabel(self.translation_frame,
                                         text = "Translation",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 300,
                                         corner_radius=10
                                         )
        
        self.rotation_frame = CTkFrame(self.test_frame)
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
                    color = "blue"
                else:
                    color = "red"

                button = CTkButton(self.translation_frame,
                    text = self.translation_buttons[i][j]["name"],
                    height = 100,
                    width = 100,
                    command = self.translation_buttons[i][j]["command"],
                    fg_color= color,
                    hover_color= "orange")
                
                button.grid(row=j+1, column=i,padx = 10, pady = 10)

        for i in range(len(self.rotation_buttons)):
            for j in range(len(self.rotation_buttons[i])):
                if i == 0:
                    color = "blue"
                else:
                    color = "red"

                button = CTkButton(self.rotation_frame,
                    text = self.rotation_buttons[i][j]["name"],
                    height = 100,
                    width = 100,
                    command = self.rotation_buttons[i][j]["command"],
                    fg_color= color,
                    hover_color= "orange")
                
                button.grid(row=j+1, column=i,padx = 10, pady = 10)


            

    
        
    # Il faut refaire les boutons connection et sequence, on les a supprimé sans faire exprès (oupsi)
        
        # self.connection_button.grid(row = 1, column = 2,columnspan = 1, padx = 10, pady = 10)
        # self.test_sequence.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.translation_frame.grid(row = 1, rowspan= 2, column = 0, padx = 10, pady = 10)
        self.rotation_frame.grid(row = 1,rowspan = 2,column = 1, padx = 10, pady = 10)





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
        self.settings_frame.place(relx=0.5, rely=0.4, anchor = "center")
    

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
                                         fg_color = "grey20",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.translation_start_label = CTkLabel(self.translation_frame,
                                         text = "Starting Point (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_end_label = CTkLabel(self.translation_frame,
                                         text = "Ending Point (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.translation_step_label = CTkLabel(self.translation_frame,
                                         text = "Step (mm)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.translation_speed_label = CTkLabel(self.translation_frame,
                                         text = "Speed (%)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
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

        self.translation_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.translation_start_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.translation_end_label.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.translation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.translation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.translation_step_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.translation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.translation_step_textbox.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.translation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = 10)
        

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
                                         fg_color = "grey20",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.rotation_start_label = CTkLabel(self.rotation_frame,
                                         text = "Starting Point (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.rotation_end_label = CTkLabel(self.rotation_frame,
                                         text = "Ending Point (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.rotation_step_label = CTkLabel(self.rotation_frame,
                                         text = "Step (°)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.rotation_speed_label = CTkLabel(self.rotation_frame,
                                         text = "Speed (%)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
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
        self.rotation_start_textbox.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.rotation_end_textbox.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.rotation_step_label.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.rotation_speed_label.grid(row = 3, column = 2, padx = 10, pady = 10)
        self.rotation_step_textbox.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.rotation_speed_textbox.grid(row = 4, column = 2, padx = 10, pady = 10)

    
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
                                         fg_color = "grey20",
                                         corner_radius=10,
                                         height = 75,
                                         width = self.section_width
                                         )
        
    
        self.exposure_time_label = CTkLabel(self.timing_frame,
                                         text = "Exposure Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        self.saving_time_label = CTkLabel(self.timing_frame,
                                         text = "Saving Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = self.section_width/2*0.8,
                                         corner_radius=10
                                         )
        
        self.margin_time_label = CTkLabel(self.timing_frame,
                                         text = "Margin Time (s)",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
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
        self.exposure_time_textbox.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.saving_time_label.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.saving_time_textbox.grid(row = 4, column = 1, padx = 10, pady = 10)

        self.margin_time_label.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.margin_time_textbox.grid(row = 6, column = 1, padx = 10, pady = 10)

        ## Validation Button

        self.confirmation_button = CTkButton(self,
                                text="Send Configuration",
                                font = ("Roboto", 20),
                                height = 75,
                                width = 400)
        
        self.confirmation_button.place(relx = 0.3, rely = 0.8, anchor = "center")

        ## Panel to verify changes made to the STM32 data

        self.verification_frame = CTkTextbox(self,
                                                width = 500,
                                                height = 150,
                                                font=("Roboto", 16)
                                                )
        self.verification_frame.place(relx = 0.7, rely = 0.8, anchor = "center")


class CapturePanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Capture")

        self.control_frame = CTkFrame(self)
        self.control_frame.place(x =100, y = 100)

        self.control_label = CTkLabel(self.control_frame,
                                         text="Control",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 300,
                                         corner_radius=10
                                         )
        self.start_button = CTkButton(self.control_frame,
                                        text="Start Capture",
                                        height = 100,
                                        width = 100)
        self.stop_button = CTkButton(self.control_frame,
                                        text="Stop Capture",
                                        height = 100,
                                        width = 100)
        self.control_label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)
        self.start_button.grid(row = 1, column = 0, padx = 20, pady = 20)
        self.stop_button.grid(row = 1, column = 1, padx = 20, pady = 20)


        self.info_frame = CTkFrame(self)
        self.info_frame.place(x=500, y=100)

        self.info_label = CTkLabel(self.info_frame,
                                         text="Capture Status",
                                         font=("Roboto", 16),
                                         fg_color = "grey30",
                                         width = 300,
                                         corner_radius=10
                                         )

        self.progress_bar = CTkProgressBar(self.info_frame,
                                            height = 30,
                                            width =500)
        
        self.position = CTkLabel(self.info_frame,
                                 text="pos : ... / 180 cm   angle : ... / 290°",
                                 font=("Roboto", 16),
                                 fg_color = "grey30",
                                 height= 50,
                                 width = 100,
                                 corner_radius=10
                                )

        self.number_frame = CTkFrame(self.info_frame)
        self.number_label = CTkLabel(self.number_frame, text="Number of Pictures")
        self.number = CTkTextbox(self.number_frame,
                                    width = 100,
                                    height=30)

        self.number_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.number.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.info_label.grid(row = 0, column =0, padx=20, pady = 20)
        self.progress_bar.grid(row = 1, column = 0, padx=20, pady=20)
        self.position.grid(row = 2, column =0, padx=20, pady = 20)
        self.number_frame.grid(row = 3, column = 0, padx=20, pady=20)
        

        self.terminal = CTkTextbox(self,
                                    width = 1000,
                                    height = 200)
        self.terminal.place(x = 100, y = 430)


        


class PanelContainer(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.width = 1500
        self.height = 900
        

        self.configure(width = self.width, height = self.height , corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.state = "Settings"
        


        self.panels = {"Move": MovePanel(self), "Test": TestPanel(self), "Settings": SettingsPanel(self), "Capture": CapturePanel(self)}
        for panel in self.panels.values():
            panel.place(x = -self.width, y = 0)
            panel.x, panel.y = -self.width, 0
        
        self.panels["Settings"].place(x =0)
        self.panels["Settings"].x = 0
        
        
        
        
        
    def setPanel(self, panel_name):
        if panel_name==self.state:
            return 0

        current_panel = self.panels[self.state]
        new_panel = self.panels[panel_name]
        current_panel.place(x=-self.width)
        new_panel.place(x=0)

        self.state = panel_name

        return 1



class Sidebar(CTkFrame):
    def __init__(self, master, panel_container):
        super().__init__(master)


        self.width = SIDEBAR_WIDTH
        self.button_height = 100
        self.button_spacing = 10


        self.configure(width=80, corner_radius=0)

        self.panel_container= panel_container
    

        self.button_container = CTkFrame(self,
                                        fg_color = "#2B2B2B")

        self.buttons = [
            {"name": "Move", "icon": "move_icon.png", "command": lambda:self.panel_container.setPanel("Move")},
            {"name": "Test", "icon": "test_icon.png", "command": lambda:self.panel_container.setPanel("Test")},
            {"name": "Capture\nSettings", "icon": "settings_icon.png", "command": lambda:self.panel_container.setPanel("Settings")},
            {"name": "Capture", "icon": "capture_icon.png", "command": lambda:self.panel_container.setPanel("Capture")},
            ]
        for element in self.buttons:
            image = Image.open("./img/"+element["icon"])
            icon = CTkImage(light_image = image,
                            dark_image=image,
                            size=(int(self.button_height*0.6),
                            int(self.button_height*0.6)))
            

            button = CTkButton(self.button_container,
                               width = self.width,
                               height = self.button_height,
                               corner_radius= 0,
                               text=element["name"],
                               image=icon,
                               compound="top",
                               command = element["command"],
                               font=("Roboto", 16),
                               text_color="#D9D9D9",
                               fg_color = "#2B2B2B",
                               hover_color="gray30")

            button.pack(anchor="nw", padx=0, pady=self.button_spacing)
            

        self.button_container.pack(anchor="ne", padx=0, pady=200)


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