import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre

import constants


class DriveSubsystems(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        # I am choosing to define these here because I belive constants should remain just numbers
        self.left1 = ctre.WPI_TalonFX(constants.LEFT_MOTOR_ID_1)
        self.left2 = ctre.WPI_TalonFX(constants.LEFT_MOTOR_ID_2)
        self.right1 = ctre.WPI_TalonFX(constants.RIGHT_MOTOR_ID_1)
        self.right2 = ctre.WPI_TalonFX(constants.RIGHT_MOTOR_ID_2)

        # Makes it so the robot doesn't move when idle, like a car in park vs neutral
        self.left1.setNeutralMode(ctre.NeutralMode.Brake)
        self.left2.setNeutralMode(ctre.NeutralMode.Brake)
        self.right1.setNeutralMode(ctre.NeutralMode.Brake)
        self.right2.setNeutralMode(ctre.NeutralMode.Brake)

        # Puts the side motors in groups so we don't have to deal with all four, just 2 for each side
        self.left = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.right = wpilib.MotorControllerGroup(self.right1, self.right2)

        self.right.setInverted(True)

        # Bascially creates a car object with both motor groups for each side
        self.drive = wpilib.drive.DifferentialDrive(
            self.left,
            self.right,
        )

        # Limits the speed that the robot will go to
        self.maxOut = constants.MAX_SPEED
        self.setMaxOutput(self.maxOut)

    def arcadeDrive(self, forward: float, rotation: float) -> None:
        """
        Run this function to make the robot move

        Args:
            forward (float): A number for the robot to move forwards or backwards (if negitive)
            rotation (float): A number for the robot to rotate, left if -1, right if 1, should not be any other numbers
        """
        self.drive.arcadeDrive(forward, -rotation)

    def setMaxOutput(self, maxOutput: float):
        """
        Is made to work with boost, allows you to increase or decrease the target
        speed of the robot

        Args:
            maxOuput (float): The max, or target, speed of the robot you want to switch to 
        """
        self.maxOut = maxOutput
        self.drive.setMaxOutput(maxOutput)
