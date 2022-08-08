from pynput import keyboard
from sysbotbase import *
from nxmapping import *

ScreenOn = True

class KeyCapture():
    def __init__(self):
        listener = keyboard.Listener(on_press = self.OnPress, on_release = self.OnRelease)
        listener.start()

    def setSwitchRemote(self, switch):
        self.switch = switch

    def OnPress(self, key):

        # Check once
        CheckValue =  key.vk if hasattr(key, "vk") else key.value.vk

        # Press button
        if CheckValue in Buttons:
            SwitchControl.SendToSwitch(self.switch, f"press {Buttons[CheckValue]}")

        # Right stick movement
        elif CheckValue in RightStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick RIGHT {RightStick[CheckValue][0]}")

        # Press special button
        elif CheckValue in NumberedKeys:
            SwitchControl.SendToSwitch(self.switch, f"click {NumberedKeys[CheckValue]}")

        # Left stick movement
        elif CheckValue in LeftStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick LEFT {LeftStick[CheckValue][0]}")

        else:
            pass


    def OnRelease(self, key):
        CheckValue = key.vk if hasattr(key, "vk") else key.value.vk

        # Release button
        if CheckValue in Buttons:
            SwitchControl.SendToSwitch(self.switch, f"release {Buttons[CheckValue]}")

        # sys-botbase controller reset
        elif CheckValue in ControllerReset:
            SwitchControl.SendToSwitch(self.switch, ControllerReset[CheckValue])

        # Right stick movement
        elif CheckValue in RightStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick RIGHT {RightStick[CheckValue][1]}")

        # Left stick movement
        elif CheckValue in LeftStick:
            SwitchControl.SendToSwitch(self.switch, f"setStick LEFT {LeftStick[CheckValue][1]}")

        # Flip between Switch screen on/off
        elif CheckValue in ScreenSettings:
            global ScreenOn
            ScreenOn = not ScreenOn

            if ScreenOn is False:
                SwitchControl.SendToSwitch(self.switch, ScreenSettings[CheckValue][0])
            else:
                SwitchControl.SendToSwitch(self.switch, ScreenSettings[CheckValue][1])

        # Other hotkeys for client end
        elif CheckValue in HotKeys:
            HotKeys[CheckValue]()

        else:
            pass