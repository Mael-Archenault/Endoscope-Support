import serial
import time
from const import *

import serial.tools.list_ports


BAUD_RATE = 115200  # Common baud rate; adjust as needed
TIMEOUT = 1  # Timeout in seconds
ser = None

def initialize_connection(port):
    try:
        # Open the serial port
        global ser
        ser = serial.Serial(port, BAUD_RATE, timeout=TIMEOUT)
        # Wait for the connection to initialize
        time.sleep(2)
        return (0, "")

    except serial.SerialException as e:
        return (-1, str(e))     

def get_available_ports():
    ports = serial.tools.list_ports.comports()
    return [port.description for port in ports]

def close_connection():
    global ser
    if ser == None:
        return (-1, "No connection is established")
    if ser.is_open:
        try:
            ser.close()
            ser = None
            return (0,"")
        except serial.SerialException as e:
            return (-1, str(e))
    return (-1, "No connection is established")


def send_command(command):
    global ser
    if ser == None:
        return (-1, "No connection is established")
    
    while len(command) <BUFF_SIZE-1:
       
        command += ' '  # Add spaces to fill up to 32 characters

    encoded_string = (command + '\0').encode('utf-8')
    try:
        ser.write(encoded_string)
        time.sleep(0.05) # Necessary time for the stm to gather all data before sending another command
        return (0,"")
    except serial.SerialException as e:
        return (-1, str(e))
   
def receive_data():
    if ser == None:
        return None
    if ser.in_waiting >= BUFF_SIZE:  # Check if data is available to read
        data = ser.read(BUFF_SIZE)  # Read a full line of data
        return data.decode('utf-8').strip("\x00")
