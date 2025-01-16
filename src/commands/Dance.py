from subsytems.driverSubsystem import DriveSubsystems
import commands2
from wpilib.shuffleboard import Shuffleboard
import time

from configGenerator import requireConfigConstant, getConstantValue
requireConfigConstant("DANCE_SPEED")
requireConfigConstant("DANCE_WAIT_TIME")

class Dance(commands2.command.Command):
    """
    The purpose of this command is the make the robot
    go back and forth while a button is being held
    """

    def __init__(self, drive: DriveSubsystems):
        self.drive = drive
        self.addRequirements(self.drive)

    def initialize(self):
        self.startTime = time.time()

    def end(self, interrupted: bool):
        pass
    
    def execute(self) -> None:
        if time.time() - self.startTime >= getConstantValue("DANCE_WAIT_TIME*2"):
            self.startTime = time.time()
            
        elif time.time() - self.startTime >= getConstantValue("DANCE_WAIT_TIME*1"):
            self.drive.arcadeDrive(-getConstantValue("DANCE_SPEED"), 0)
        else:
            self.drive.arcadeDrive(getConstantValue("DANCE_SPEED"), 0)
        
