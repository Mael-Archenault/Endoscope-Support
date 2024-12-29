from customtkinter import *
from PIL import Image, ImageTk

def testfunc():
    print("Test function called")

class ControlPanel(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.topbar = Topbar(self)
        self.topbar.grid(row=0, column=1,columnspan=2, sticky="w")
        
        self.grid_columnconfigure(0, weight=1)
        self.checkboxes = []
        self.state = None
        self.title = CTkLabel(self)


        self.configure(fg_color="#D9D9D9", corner_radius=0)
        self.setMoveState()
        
        

        


    def setMoveState(self):
        if self.state != "Move":
            self.state = "Move"
            self.title.destroy()
            self.title = CTkLabel(self, text="Move",  fg_color="gray30", corner_radius=6, font=("Roboto", 20))
            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

    def setTestState(self):
        if self.state != "Test":
            self.state = "Test"
            self.title.destroy()
            self.title = CTkLabel(self, text="Test", fg_color="gray30", corner_radius=6, font=("Roboto", 20))
            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
    
    def setSettingsState(self):
        if self.state != "Settings":
            self.state = "Settings"
            self.title.destroy()
            self.title = CTkLabel(self, text="Capture Settings", fg_color="gray30", corner_radius=6, font=("Roboto", 20))
            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

    def setCaptureState(self):
        if self.state != "Capture":
            self.state = "Capture"
            self.title.destroy()
            self.title = CTkLabel(self, text="Capture", fg_color="gray30", corner_radius=6, font=("Roboto", 20))
            self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")






class Sidebar(CTkFrame):
    def __init__(self, master, control_panel):
        super().__init__(master)
        self.configure(fg_color="#FEF7FF", width=80, corner_radius=0)

        self.control_panel= control_panel
    

        self.button_container = CTkFrame(self)
        self.button_container.configure(fg_color="#FEF7FF")

        self.buttons = [
            {"name": "Move", "icon": "move_icon.png", "command": self.control_panel.setMoveState},
            {"name": "Test", "icon": "test_icon.png", "command": self.control_panel.setTestState},
            {"name": "Capture\nSettings", "icon": "settings_icon.png", "command": self.control_panel.setSettingsState},
            {"name": "Capture", "icon": "capture_icon.png", "command": self.control_panel.setCaptureState},
            ]
        for element in self.buttons:
            image = Image.open("./img/"+element["icon"])
            
            # Get pixel data
            pixels = image.load()
            width, height = image.size

            # Iterate through all pixels
            for y in range(height):
                for x in range(width):
                    
                    r, g, b, a = pixels[x, y]  # Get RGBA values
                    if a != 0:  # If the pixel is not fully transparent
                        pixels[x, y] = (74,68,89,255)  # Replace with target color


            icon = CTkImage(light_image=image, dark_image=image)
            

            button = CTkButton(self.button_container, width = 80, height = 56, corner_radius= 0, text=element["name"],image=icon, compound="top", command = element["command"], fg_color="#FEF7FF", font=("Roboto", 16), text_color="#4A4459", hover_color="#D9D9D9")
            button.pack(anchor="nw", padx=0, pady=10)
            

        self.button_container.pack(anchor="ne", padx=0, pady=200)


class Topbar(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#D9D9D9", height=50, corner_radius=0)
        
        image = Image.open("./img/settings_icon.png")
        image = image.resize((50,50))
        icon = ImageTk.PhotoImage(image)
        self.settings_button = CTkButton(self,image = icon, width = 10, height = 10, corner_radius= 40, text="", fg_color="#4A4459", hover_color="#817d8c", border_width=5, border_color="#4A4459")
        self.settings_button.pack(side="right", anchor="ne", padx=10, pady=10)

        

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Endoscope Application")
        self.geometry("1600x900")
        self.minsize(1080,720)
        self.grid_columnconfigure(1, weight=1)
       
        self.grid_rowconfigure(0, weight=1)


        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=1, sticky="nsew")


        self.sidebar = Sidebar(self, self.control_panel)
        self.sidebar.grid(row=0, column=0, rowspan=2 , sticky="nsew")
        
        
app = App()
app.mainloop()