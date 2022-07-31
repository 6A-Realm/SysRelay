import ctypes
import socket
import cv2
from pynput import keyboard
from nxmapping import *
import os
from threading import Thread

# Open terminal
ctypes.windll.kernel32.SetConsoleTitleW("SysRelay")

SwitchIP = input("Enter your Switch's IP: ")
ScreenOn = True

# Show controller mapping
ControllerImage = cv2.imread('controller.png')
cv2.imshow(f"TCP: {SwitchIP}", ControllerImage)
cv2.waitKey(1)

# Broadcast Switch screen
def SwitchRecord():

    SwitchScreen = cv2.VideoCapture(f"rtsp://root:pass@{SwitchIP}:6666//rtplive/_definst_/hessdalen03.stream")

    while(SwitchScreen.isOpened()):
        ret, frame = SwitchScreen.read()
        cv2.imshow(f"RSTP: {SwitchIP}", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    SwitchScreen.release()
    cv2.destroyAllWindows()

# Create socket connection
switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
switch.connect((SwitchIP, 6000))

# Command to switch parser
def SendToSwitch(command):
    command += "\r\n"
    switch.sendall(command.encode())

# When key is pressed
def OnPress(key):

    # Check if key has associated character
    if hasattr(key, 'char') and key.char != None:

        # Press button
        if key.char.upper() in buttons:
                SendToSwitch(f"press {buttons[key.char.upper()]}")

        # Right Stick
        if key.char.upper() in RightStick:
            SendToSwitch(f"setStick RIGHT {RightStick[key.char.upper()][0]}")
            SendToSwitch(f"setStick RIGHT {RightStick[key.char.upper()][1]}")

    # Check if key has associated number
    elif hasattr(key, 'vk') and str(key.vk) in NumberedKeys:
        SendToSwitch(f"click {NumberedKeys[str(key.vk)]}")

    # Check if key has associated value
    elif hasattr(key, '_value_') and str(key._value_)[1:-1] in LeftStick:

            # Left Stick
            SendToSwitch(f"setStick LEFT {LeftStick[str(key._value_)[1:-1]][0]}")
            SendToSwitch(f"setStick LEFT {LeftStick[str(key._value_)[1:-1]][1]}")
    else:
        pass


# When key is released
def OnRelease(key):
    try:
        if key.char.upper() in buttons:
            SendToSwitch(f"release {buttons[key.char.upper()]}")

    except AttributeError:

        # Kill SysRelay
        if key == keyboard.Key.esc:
            return os._exit(1)

        if key == keyboard.Key.caps_lock:
            SendToSwitch("configure controllerType 3")

        if key == keyboard.Key.page_up:
            global ScreenOn
            ScreenOn = not ScreenOn
            if ScreenOn is False:
                SendToSwitch("screenOff")
            else:
                SendToSwitch("screenOn")


listener = keyboard.Listener(on_press = OnPress, on_release = OnRelease)
listener.start()

Thread(target = SwitchRecord).start()