import socket
import cv2
from pynput import keyboard


vkToSwitch = {
    "buttons": {
        # Action Buttons
        "Z": "X",
        "A": "A",
        "S": "B",
        "J": "X",
        # Split D-Pad
        "T": "DUP",
        "H": "DRIGHT",
        "G": "DDOWN",
        "F": "DLEFT",
        # Bumper Buttons
        "Q": "L",
        "W": "R",
        # Special Buttons
        "M": "MINUS",
        "N": "PLUS",
        "V": "CAPTURE",
        "B": "HOME"
    },
    "NumberedKeys": {
        "97": "ZL",
        "98": "ZR",
        "99": "LSTICK",
        "100": "RSTICK"
    },
    "RightStick": {
        "I": ["yVal 0x7FFF", "yVal 0x0000"],
        "L": ["0x7FFF 0x0", "0x0 0x0"],
        "K": ["yVal -0x8000", "yVal 0x0000"],
        "J": ["-0x8000 0x0", "0x0 0x0"]
    },
    "LeftStick": {
        "38": ["yVal 0x7FFF", "yVal 0x0000"],
        "39": ["0x7FFF 0x0", "0x0 0x0"],
        "40": ["yVal -0x8000", "yVal 0x0000"],
        "37": ["-0x8000 0x0", "0x0 0x0"]
    }
}


class SwitchStream():
    def __init__(self, ip):
        self.ip = ip
        self.stream = None

    def showStream(self):
        print("Streaming from " + self.ip)
        self.stream = cv2.VideoCapture(
            f"rtsp://root:pass@{self.ip}:6666//rtplive/_definst_/hessdalen03.stream")
        while(self.stream.isOpened()):
            ret, frame = self.stream.read()
            cv2.imshow(f"SwScr", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        self.stream.release()
        cv2.destroyAllWindows()


class KeyCapture():
    def __init__(self):
        listener = keyboard.Listener(on_press=self.OnPress)
        listener.start()
        switch = None

    def setSwitchRemote(self, switch):
        self.switch = switch

    def get_vk(self, key):
        return key.vk if hasattr(key, 'vk') else key.value.vk

    def OnPress(self, key):
        pressedKey = key
        VK = self.get_vk(key)
        print(f"Pressed: {VK}, {pressedKey}")

      

    def OnRelease(self, key):
        pass


class SwitchControl():
    def __init__(self, ip):
        return
        self.switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.switch.connect((ip, 6000))

    def SendToSwitch(self, command):
        print(f"Sending to switch: {command}")
        return
        command += "\r\n"
        self.switch.sendall(command.encode())




"""

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

"""