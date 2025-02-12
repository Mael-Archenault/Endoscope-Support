import serial
import time

# Replace 'COM3' with the correct port for your USB device
PORT = 'COM3'
BAUD_RATE = 115200  # Common baud rate; adjust as needed
TIMEOUT = 1  # Timeout in seconds

try:
    # Open the serial port
    ser = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)
    print(f"Connected to {PORT} at {BAUD_RATE} baud.")

    # Wait for the connection to initialize
    time.sleep(2)

    while True:
        # Get a string input from the user
        string_to_send = input("Enter a string to send via USB (type 'exit' to quit): ")
        while len(string_to_send) <32:
            string_to_send += ' '  # Add spaces to fill up to 32 characters
        # Exit condition
        if string_to_send.lower() == 'exit':
            print("Exiting...")
            break

        # Send the string with a newline character
        encoded_string = (string_to_send + '\0').encode('utf-8')
        
        ser.write(encoded_string)
        print(f"Sent {len(encoded_string)} bytes: {string_to_send}")

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    # Close the serial port when done
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print(f"Disconnected from {PORT}.")
