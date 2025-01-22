from photonlibpy.photonCamera import PhotonCamera
from commands2 import Subsystem
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget

from configGenerator import requireConfigConstant, cget
requireConfigConstant("CAMERA_NAME")

class AprilTagSubsystem(Subsystem): # Apriltags with PhotonVision
    def __init__(self) -> None:
        super().__init__()

        self.cam = PhotonCamera(cget("CAMERA_NAME"))
        self.flagOn = False
        self.flag = None
        self.targets = []

    def getHighestID(self, targets: list[PhotonTrackedTarget]) -> PhotonTrackedTarget: # get the target with the highest fiducial ID
        bestTarget = targets[0]
        for target in targets:
            if target.getFiducialId() > bestTarget.getFiducialId():
                bestTarget = target
        return bestTarget

    def refresh(self) -> list[PhotonTrackedTarget]: # Get latest target data
        result = self.cam.getLatestResult()
        if result.hasTargets():
            self.targets = result.getTargets()
            return self.targets
        else: 
            self.targets = None  

    def hasTarget(self, id: int = None) -> bool: # See if a target with a given fiducial is visible. Run with no args to see if any targets are visible
        targets = self.targets
        if targets is None:
            return False
        
        if id is None: 
            return True # If no id is given and we have targets
        
        for target in targets:
            if target.getFiducialId() == id:
                return True # If target is found
                
        return False # No targets
    
    def getTargetYaw(self, id:int): # Get the angle of the target so we can steer towards it
        targets = self.targets
        if targets is not None:
            for target in targets:
                if target.getFiducialId() == id:
                    return target.getYaw()
        return 0
    
    def setFlag(self, flag):
        self.flagOn = True
        self.flag = flag

    def isFlagged(self):
        return self.flagOn
