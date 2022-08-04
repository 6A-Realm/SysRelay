from sysdvr import SwitchStream
from sysbotbase import *
from keytranslator import *
import threading
import re

# Check if IP is valid using Regex
SwitchIP = input("Enter your Switch's IP: ")

# Change this IP to your IP for quick load
if SwitchIP == "": SwitchIP = "10.0.0.165"

if not re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", SwitchIP):
    print("Invalid IP entered.")
    exit()


def StreamThread():
    stream = SwitchStream(SwitchIP)
    stream.showStream()

# Create thread
thread = threading.Thread(target = StreamThread)
thread.start()

# Load
RC = SwitchControl(SwitchIP)
KC = KeyCapture()
KC.setSwitchRemote(RC)