import typing
import commands2
from subsytems.driverSubsystem import DriveSubsystems

class DefaultDrive(commands2.Command):
    def __init__(
        self,
        drive: DriveSubsystems,
        forward: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
        speed: typing.Callable[[], float]
    ) -> None:
        super().__init__()

        self.drive = drive
        self.forward = forward
        self.rotation = rotation
        self.speed = speed

        self.addRequirements(self.drive)
        
    def execute(self) -> None:
        self.drive.arcadeDrive(self.forward()*self.speed(), self.rotation()*self.speed())
