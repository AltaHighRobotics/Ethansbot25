#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
from commands.forward import DefaultDrive
from subsytems.driverSubsystem import DriveSubsystems
from commands.Search import Search
from commands.autoAlign import AutoAlign
from subsytems.apriltagSubsystem import AprilTagSubsystem
import InputManager
import wpilib
from commands.Dance import Dance

# from commands2.defaultDrive import DefaultDrive
import commands2

from configGenerator import requireConfigConstant, cget
requireConfigConstant("REGULAR_SPEED")
requireConfigConstant("ROTATION_SPEED")

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self.drive = DriveSubsystems()
        self.vision = AprilTagSubsystem()

        # This code SHOULD run every frame while the robot is active
        self.drive.setDefaultCommand(DefaultDrive(self.drive, cget("REGULAR_SPEED"), cget("ROTATION_SPEED")))

        # We want it to dance while holding the left bumper
        InputManager.onButtonHold(InputManager.Button.LEFT_BUMPER, lambda: Dance(self.drive))

        self.vision.setDefaultCommand(Search(self.vision))
        commands2.button.Trigger(lambda: self.vision.hasTarget(1)).whileTrue(AutoAlign(self.drive, self.vision, 1))

    def getAutonomousCommand(self) -> str:
        return ""

