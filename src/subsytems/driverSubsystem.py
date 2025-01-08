import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre

import constants



class DriveSubsystems(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.left1 = ctre.WPI_TalonFX(constants.LEFT_MOTOR_ID_1)
        self.left2 = ctre.WPI_TalonFX(constants.LEFT_MOTOR_ID_2)
        self.right1= ctre.WPI_TalonFX(constants.RIGHT_MOTOR_ID_1)
        self.right2= ctre.WPI_TalonFX(constants.RIGHT_MOTOR_ID_2)

        self.left1.setNeutralMode(ctre.NeutralMode.Brake)
        self.left2.setNeutralMode(ctre.NeutralMode.Brake)
        self.right1.setNeutralMode(ctre.NeutralMode.Brake)
        self.right2.setNeutralMode(ctre.NeutralMode.Brake)

        self.left = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.right = wpilib.MotorControllerGroup(self.right1, self.right2)

        self.right.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(
            self.left,
            self.right,
        )

        self.maxOut = constants.MAX_SPEED
        self.setMaxOutput(self.maxOut)

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        self.drive.arcadeDrive(fwd, -rot)

    def setMaxOutput(self, maxOutput: float):
        self.maxOut = maxOutput
        self.drive.setMaxOutput(maxOutput)
