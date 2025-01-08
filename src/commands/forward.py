import typing
import commands2
import InputManager
from subsytems.driverSubsystem import DriveSubsystems


class DefaultDrive(commands2.Command):
    def __init__(self, drive: DriveSubsystems, speed: float) -> None:
        super().__init__()

        self.drive = drive
        self.speed = speed

        self.addRequirements(self.drive)

    def execute(self) -> None:
        forward = InputManager.getGasVsReverse()
        rotation = InputManager.getHorizontalStick()

        self.drive.arcadeDrive(forward * self.speed, rotation * self.speed)
