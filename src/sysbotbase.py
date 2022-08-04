import socket
from rich.console import Console

console = Console()

class SwitchControl():
    def __init__(self, SwitchIP):
        try:
            self.switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.switch.connect((SwitchIP, 6000))
            console.print(f"Sending commands to {SwitchIP}.", style = "green")
        except:
            console.print(f"Unable to connect to {SwitchIP}.", style = "red")

    def SendToSwitch(self, command):
        try:
            command += "\r\n"
            self.switch.sendall(command.encode())
        except Exception as e: 
            console.print(f"Unable to send commands to switch. {e}", style = "red")