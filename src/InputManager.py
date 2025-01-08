import wpilib
from enum import Enum
import constants
from typing import Callable


class Button(Enum):
    LEFT_BUMPER = 5


driverController = wpilib.XboxController(constants.kDriverControllerPort)
# self.driverController = wpilib.Joystick(constants.kDriverControllerPort)


def getGasVsReverse() -> float:
    return (
        driverController.getRightTriggerAxis() - driverController.getLeftTriggerAxis()
    )


def getHorizontalStick() -> float:
    return min(1, max(-1, driverController.getLeftX() + driverController.getRightX()))


def onButtonHold(button: Button, function: Callable):
    commands2.button.JoystickButton(driverController, button).whileTrue(function())
