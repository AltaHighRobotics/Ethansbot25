import typing
import commands2
import InputManager
from subsytems.driverSubsystem import DriveSubsystems


class DefaultDrive(commands2.Command):
    """
    The purpose of this command is to allow the robot
    to move backwards, forwards and rotate from controller input
    """

    def __init__(self, drive: DriveSubsystems, speed: float, rotationSpeed: float) -> None:
        super().__init__()

        self.drive = drive
        self.speed = speed
        self.rotationSpeed = rotationSpeed

        self.addRequirements(self.drive)

    def execute(self) -> None:
        forward = InputManager.getGasVsReverse()
        rotation = InputManager.getHorizontalStick()

        self.drive.arcadeDrive(forward * self.speed, rotation * self.rotationSpeed)
