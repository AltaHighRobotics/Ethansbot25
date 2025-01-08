#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
from commands.forward import DefaultDrive
from subsytems.driverSubsystem import DriveSubsystems
import InputManager
import constants
import wpilib
from commands.Dance import Dance
import constants

# from commands2.defaultDrive import DefaultDrive
import commands2


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self.drive = DriveSubsystems()

        self.drive.setDefaultCommand(DefaultDrive(self.drive, 1))

        InputManager.onButtonHold(InputManager.Button.LEFT_BUMPER, Dance(self.drive))

    def getAutonomousCommand(self) -> str:
        return ""
