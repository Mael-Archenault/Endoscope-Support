from customtkinter import *
from PIL import Image


def testfunc():
    print("Test function called")


class Panel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.width = 1450
        self.height = 850
        self.x, self.y = 0,0
        self.title = CTkLabel(self,width=int(self.width*0.9), text="",  fg_color="gray30", corner_radius=6, font=("Roboto", 20))
        self.title.place(relx =0.5, y = 50/2, anchor = "center")
        self.configure(width=self.width, height=self.height, corner_radius = 20, bg_color="transparent")


class MovePanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Move")

class TestPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Test")

class SettingsPanel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Capture Settings")

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
        self.info_frame.place(x=700, y=100)

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

        self.number_frame = CTkFrame(self.info_frame)
        self.number_label = CTkLabel(self.number_frame, text="Number of Pictures")
        self.number = CTkTextbox(self.number_frame,
                                    width = 100,
                                    height=30)

        self.number_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.number.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.info_label.grid(row = 0, column =0, padx=20, pady = 20)
        self.progress_bar.grid(row = 1, column = 0, padx=20, pady=20)
        self.number_frame.grid(row = 2, column = 0, padx=20, pady=20)

        self.terminal = CTkTextbox(self,
                                    width = 1000,
                                    height = 400)
        self.terminal.place(x = 100, y = 400)

class Panel(Panel):
    def __init__(self, master):
        super().__init__(master)
        self.title.configure(text="Move")

        


class PanelContainer(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.width = 1500
        self.height = 900
        

        self.configure(width = self.width, height = self.height , corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.state = "Move"
        


        self.panels = {"Move": MovePanel(self), "Test": TestPanel(self), "Settings": SettingsPanel(self), "Capture": CapturePanel(self)}
        for panel in self.panels.values():
            panel.place(relx = 0.5, rely = 0.5, x=-self.width, y = 0, anchor = "center")
            panel.x, panel.y = -self.width, 0
        
        self.panels["Capture"].place(x =0)
        self.panels["Capture"].x = 0
        
        
        
        
        
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


        self.width = 100
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
        self.geometry("1600x900")
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
       
        self.grid_rowconfigure(0, weight=1)

        self.panel_container = PanelContainer(self)
        self.panel_container.place(x = 100, y = 0)


        self.sidebar = Sidebar(self, self.panel_container)
        self.sidebar.place(x = 0, y = 0)

        self.settings_button = SettingsButton(self)
        self.settings_button.place(relx=0.9, rely=0.9, anchor = "center")
        
        
        
app = App()
app.mainloop()