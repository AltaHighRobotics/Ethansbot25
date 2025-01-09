from commands2 import Command
from wpimath.controller import PIDController
from typing import Callable
import InputManager

from subsytems.driverSubsystem import DriveSubsystems
from subsytems.apriltagSubsystem import AprilTagSubsystem

import constants
        # AutoAlign(self.drive, self.vision, lambda: , lambda: , 1))

class AutoAlign(Command):
    def __init__(self, drive: DriveSubsystems, vision: AprilTagSubsystem, tagID = 1):
        super().__init__()

        self.drive = drive
        self.vision = vision
        self.tagnID = tagID

        self.PID = PIDController(constants.AUTO_ALIGN_P, constants.AUTO_ALIGN_I, constants.AUTO_ALIGN_D)
        self.PID.disableContinuousInput()
        self.PID.setSetpoint(0)

    def execute(self):
        forward = InputManager.getGasVsReverse()
        rotation = InputManager.getHorizontalStick()

        if self.vision.hasTarget(self.tagnID) and (abs(rotation) <= .1) :
            yaw = self.vision.getTargetYaw(self.tagnID)
            
            steerPID = self.PID.calculate(yaw)
            print(steerPID)
            
            self.drive.arcadeDrive(forward, -steerPID/12)
        
        else:
            self.drive.arcadeDrive(forward, rotation)