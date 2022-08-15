import os
import cv2

ShowMapping = False

# Kill SysRelay
def KillSysRelay():
    return os._exit(1)

# Show controller mapping
def ToggleControllerMapping():

        global ShowMapping
        ShowMapping = not ShowMapping

        if ShowMapping is True:
            ControllerImage = cv2.imread("assets/controller.png")
            cv2.imshow("Controller Mapping", ControllerImage)
            cv2.waitKey(0)

        else:
            cv2.destroyWindow("Controller Mapping")