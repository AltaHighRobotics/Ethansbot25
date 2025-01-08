import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre

import constants



class DriveSubsystems(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.left1 = constants.LEFT_MOTOR_1
        self.left2 = constants.LEFT_MOTOR_2
        self.right1 = constants.RIGHT_MOTOR_1
        self.right2 = constants.RIGHT_MOTOR_2

        self.left = constants.LEFT_SIDE
        self.right = constants.RIGHT_SIDE
        

        self.right.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(
            self.left,
            self.right,
        )

        self.maxOut = 0.5
        self.setMaxOutput(constants.MAX_SPEED)

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        self.drive.arcadeDrive(fwd, -rot)

    def setMaxOutput(self, maxOutput: float):
        self.maxOut = maxOutput
        self.drive.setMaxOutput(maxOutput)
