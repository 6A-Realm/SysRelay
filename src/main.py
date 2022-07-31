from custom import *
import threading, re

switchIP = input("Enter your Switch's IP: ")
# check if ip is valid with regex
if switchIP == "":
    switchIP = "192.168.1.4"

if not re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", switchIP):
    print("Invalid IP")
    exit()


def thread_stream():
    stream = SwitchStream(switchIP)
    stream.showStream()

# create thread
thread = threading.Thread(target=thread_stream)
thread.start()


RC = SwitchControl(switchIP)
KC = KeyCapture()
KC.setSwitchRemote(RC)
