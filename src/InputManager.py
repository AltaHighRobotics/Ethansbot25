import wpilib
from enum import Enum
import constants
from typing import Callable


class Button(Enum):
    LEFT_BUMPER = 5


# Keeping driverController as a global variable
driverController = wpilib.XboxController(constants.kDriverControllerPort)
# self.driverController = wpilib.Joystick(constants.kDriverControllerPort)


def getGasVsReverse() -> float:
    """
    Is meant to allow a robot to move forwards or backwards based on the triggers
    being fowards and backwards

    The left trigger is backwards and the right trigger is fowards

    Returns:
        float: A value between 0.5 to 1 OR -0.5 to -1
    """
    return (
        driverController.getRightTriggerAxis() - driverController.getLeftTriggerAxis()
    )


def getHorizontalStick() -> int:
    """
    Is meant for robots turing left or right based on the stick
    being flicked to the left or right

    Returns:
        int: Either 1 for right or -1 for left
    """
    return int(
        min(1, max(-1, driverController.getLeftX() + driverController.getRightX()))
    )


def onButtonHold(button: Button, function: Callable):
    """
    Runs a given function if a button is being pressed

    Args:
        button (Button): A controller button from the Button enum
        function (Callable): A function to be ran every frame the button is being held
    """

    commands2.button.JoystickButton(driverController, button).whileTrue(function())
