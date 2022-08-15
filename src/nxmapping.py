from hotkeys import *
# Button Mapping
Buttons = {

    # Action Buttons
    90: "X",
    65: "A",
    83: "B",
    88: "Y",

    # Split D-Pad
    84: "DUP",
    72: "DRIGHT",
    71: "DDOWN",
    70: "DLEFT",

    # Bumper Buttons
    81: "L",
    87: "R",

    # Special Buttons
    77: "MINUS",
    78: "PLUS",
    86: "CAPTURE",
    66: "HOME"

}

NumberedKeys = {

    97: "ZL",
    98: "ZR",
    99: "LSTICK",
    100: "RSTICK"

}

RightStick = {

    73: ["yVal 0x7FFF", "yVal 0x0000"], 
    76: ["0x7FFF 0x0", "0x0 0x0"], 
    75: ["yVal -0x8000", "yVal 0x0000"],
    74: ["-0x8000 0x0", "0x0 0x0"]

}

LeftStick = {

    38: ["yVal 0x7FFF", "yVal 0x0000"], 
    39: ["0x7FFF 0x0", "0x0 0x0"], 
    40: ["yVal -0x8000", "yVal 0x0000"],
    37: ["-0x8000 0x0", "0x0 0x0"]

}

ControllerReset = {

    20: "configure controllerType 3"

}

ScreenSettings = {

    33: ["screenOff", "screenOn"]

}

HotKeys = {

    27: KillSysRelay,
    8: ToggleControllerMapping

}