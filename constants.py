
import phoenix5 as ctre
import wpilib
import wpilib.drive

# Motors
kLeftMotor1ID = 1
kLeftMotor2ID = 2
kRightMotor1ID = 3
kRightMotor2ID = 4


# Operator Interface
kDriverControllerPort = 0
kRegSpeed = .5
kBoostSpeed = .9

LEFT_MOTOR_1 = ctre.WPI_TalonFX(kLeftMotor1ID)
LEFT_MOTOR_2 = ctre.WPI_TalonFX(kLeftMotor2ID)
RIGHT_MOTOR_1 = ctre.WPI_TalonFX(kRightMotor1ID)
RIGHT_MOTOR_2 = ctre.WPI_TalonFX(kRightMotor2ID)

LEFT_MOTOR_1.setNeutralMode(ctre.NeutralMode.Brake)
LEFT_MOTOR_2.setNeutralMode(ctre.NeutralMode.Brake)
RIGHT_MOTOR_1.setNeutralMode(ctre.NeutralMode.Brake)
RIGHT_MOTOR_2.setNeutralMode(ctre.NeutralMode.Brake)

LEFT_SIDE = wpilib.MotorControllerGroup(LEFT_MOTOR_1, LEFT_MOTOR_2)
RIGHT_SIDE = wpilib.MotorControllerGroup(RIGHT_MOTOR_1, RIGHT_MOTOR_2)

MAX_SPEED = 0.5
