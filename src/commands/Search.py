from commands2 import Command

from subsytems.apriltagSubsystem import AprilTagSubsystem

class Search(Command):
    def __init__(self, vision: AprilTagSubsystem):
        super().__init__()

        self.vision = vision
        self.addRequirements(self.vision)
    
    def execute(self):
        self.vision.refresh()