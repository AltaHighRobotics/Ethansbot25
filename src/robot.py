#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2

from wpilib.shuffleboard import Shuffleboard
from configGenerator import configData, load

from robotContainer import RobotContainer
class MyRobot(commands2.TimedCommandRobot):
    """
    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be used for any
        initialization code.
        """
        load()
        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.container = RobotContainer()
        #wpilib.CameraServer.launch("vision.py")

        # Shuffleboard
        # for scriptname, constants in configData.items():
        #     for constant, value in constants.items():
        #         self.shuffleboard = Shuffleboard.getTab(scriptname)
        #         v = self.shuffleboard.add(constant, value).withPosition(0, 0).getEntry()
        #         print(v.getDouble(1.0))
