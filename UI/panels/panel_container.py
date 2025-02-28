from customtkinter import *
import tkinter as tk
import time

from const import *

from panels.connection_panel  import ConnectionPanel
from panels.test_panel import TestPanel
from panels.settings_panel import SettingsPanel
from panels.capture_panel import CapturePanel



class PanelContainer(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master
        self.width = WINDOW_WIDTH - SIDEBAR_WIDTH
        self.height = WINDOW_HEIGHT
        

        self.configure(width = self.width, height = self.height , corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.state = "Settings"
        


        self.panels = {"Connection": ConnectionPanel(self), "Test": TestPanel(self), "Settings": SettingsPanel(self), "Capture": CapturePanel(self)}
        for panel in self.panels.values():
            panel.place(relx = -1, rely = 0.5, anchor = "center")
            panel.x, panel.y = -self.width, 0
        
        self.panels["Connection"].place(relx = 0.5, rely = 0.5, anchor = "center")
        self.panels["Connection"].x = 0
        
        
        
        
        
    def setPanel(self, panel_name):
        if panel_name==self.state:
            return 0

        current_panel = self.panels[self.state]
        new_panel = self.panels[panel_name]
        current_panel.place(relx = -1)
        new_panel.place(relx = 0.5)
        self.state = panel_name

        return 1
    
    def update_data(self, data):
        target, content = data.split(" ", 1)

        if target == "logTest":
            self.panels["Test"].display_log(content)

        if target == "logSettings":
            self.panels["Settings"].display_log(content)
        if target == "logCapture":
            self.panels["Capture"].display_log(content) 

        if target == "firmware":
            self.panels["Connection"].change_value("firmware_version_value", content, "disabled")
            self.panels["Connection"].display_log("Got the Firmware version :" + content)
            
        if target == "position":
            self.panels["Capture"].change_value("x_value", content.split(" ")[0] + " mm", "disabled")
            self.panels["Capture"].change_value("theta_value", content.split(" ")[1] + " °", "disabled")

            self.panels["Test"].change_value("x_value", content.split(" ")[0] + " mm", "disabled")
            self.panels["Test"].change_value("theta_value", content.split(" ")[1] + " °", "disabled")
        if target == "total":
            t_end, r_end, nb_pictures_for_one_angle, nb_angles, nb_total_pictures = content.split(" ")
            capture = self.panels["Capture"]
            capture.x_label_mm.configure(text = "/" + t_end + " mm")
            capture.theta_label_degree.configure(text = "/" + r_end + "°")

            capture.total_nb_pictures_angle_label.configure(text = "/"+nb_pictures_for_one_angle)
            capture.total_nb_pictures_label.configure(text = "/"+nb_total_pictures)
            capture.total_explored_angles_label.configure(text = "/"+nb_angles)

            capture.total_pictures = nb_total_pictures

            
        if target == "progress":
            pictures_taken, pictures_taken_from_this_angle, angles_explored = content.split(" ")
            
            capture = self.panels["Capture"]
            capture.change_value("nb_pictures_value", pictures_taken, "disabled")
            capture.change_value("nb_pictures_angle_value", pictures_taken_from_this_angle, "disabled")
            capture.change_value("explored_angles_value", angles_explored, "disabled")


            progress = float(pictures_taken) / float(capture.total_pictures)
            capture.progress_bar.set(progress)
            capture.progress_percentage.configure(text = str(round(progress * 100, 2)) + "%")     
            
        if target == "end":
            capture = self.panels["Capture"]
            test = self.panels["Test"]
            if content == "capture":
                capture.state = "STOPPED"
                test.state = "STOPPED"
                capture.change_value("estimated_time_value", "00:00:00", "disabled")
            if content == "testSequence":
                capture.state = "STOPPED"
                test.state = "STOPPED"


        if target == "estimatedTime":
            local_time = int(content)
            self.panels["Capture"].total_time = int(local_time)

            hours = int(local_time/3600)
            local_time%=3600
            minutes = int(local_time/60)
            local_time%=60
            seconds = int(local_time)
            self.panels["Settings"].change_value("estimated_time_value", str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2), "disabled")