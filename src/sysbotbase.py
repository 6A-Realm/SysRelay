import socket

class SwitchControl():
    def __init__(self, SwitchIP):
        try:
            self.switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.switch.connect((SwitchIP, 6000))
            print(f"Sending commands to {SwitchIP}.")
        except:
            print(f"Unable to connect to {SwitchIP}.")

    def SendToSwitch(self, command):
        try:
            command += "\r\n"
            self.switch.sendall(command.encode())
        except Exception as e: 
            print(f"Unable to send commands to switch. {e}")