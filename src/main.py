from sysdvr import SwitchStream
from sysbotbase import SwitchControl, KeyCapture
import threading, re

SwitchIP = input("Enter your Switch's IP: ")
# check if ip is valid with regex
if SwitchIP == "":
    SwitchIP = "192.168.1.4"

if not re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", SwitchIP):
    print("Invalid IP entered.")
    exit()


def thread_stream():
    stream = SwitchStream(SwitchIP)
    stream.showStream()

# create thread
thread = threading.Thread(target = thread_stream)
thread.start()


RC = SwitchControl(SwitchIP)
KC = KeyCapture()
KC.setSwitchRemote(RC)
