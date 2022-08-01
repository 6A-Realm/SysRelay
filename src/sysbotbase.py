import socket
import cv2
from pynput import keyboard
from nxmapping import *
import os

ScreenOn = True
ShowMapping = False

class SwitchControl():
    def __init__(self, SwitchIP):

        self.switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.switch.connect((SwitchIP, 6000))

    def SendToSwitch(self, command):
        command += "\r\n"
        self.switch.sendall(command.encode())

class KeyCapture():
    def __init__(self):
        listener = keyboard.Listener(on_press = self.OnPress, on_release = self.OnRelease)
        listener.start()
        switch = None

    def setSwitchRemote(self, switch):
        self.switch = switch

    def OnPress(self, key):

        # Check once
        CheckValue = hasattr(key, "vk")

        # Press button
        if CheckValue and key.vk in Buttons:
            SwitchControl.SendToSwitch(self.switch, f"press {Buttons[key.vk]}")

        # Right stick movement
        elif CheckValue and key.vk in RightStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick RIGHT {RightStick[key.vk][0]}")
            SwitchControl.SendToSwitch(self.switch, f"setStick RIGHT {RightStick[key.vk][1]}")

        # Press special button
        elif CheckValue and key.vk in NumberedKeys:
            SwitchControl.SendToSwitch(self.switch, f"click {NumberedKeys[key.vk]}")

        # Left stick movement
        elif hasattr(key, "value") and key.value.vk in LeftStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick LEFT {LeftStick[key.value.vk][0]}")
            SwitchControl.SendToSwitch(self.switch, f"setStick LEFT {LeftStick[key.value.vk][1]}")

        else:
            pass


    def OnRelease(self, key):
        CheckValue = hasattr(key, "vk")
        if CheckValue and key.vk in Buttons:
            SwitchControl.SendToSwitch(self.switch, f"release {Buttons[key.vk]}")

        # Kill SysRelay
        elif key == keyboard.Key.esc:
            return os._exit(1)

        # Reconfigure sys-botbase controller type
        elif key == keyboard.Key.caps_lock:
            SwitchControl.SendToSwitch(self.switch, "configure controllerType 3")

        # Turn screen on/off
        elif key == keyboard.Key.page_up:
            global ScreenOn
            ScreenOn = not ScreenOn

            if ScreenOn is False:
                SwitchControl.SendToSwitch(self.switch, "screenOff")
            else:
                SwitchControl.SendToSwitch(self.switch, "screenOn")

        # Show controller mapping
        elif key == keyboard.Key.backspace:
            global ShowMapping
            ShowMapping = not ShowMapping

            if ShowMapping is True:
                ControllerImage = cv2.imread("assets/controller.png")
                cv2.imshow("Controller Mapping", ControllerImage)
                cv2.waitKey(0)

            else:
                cv2.destroyWindow("Controller Mapping")

        else:
            pass