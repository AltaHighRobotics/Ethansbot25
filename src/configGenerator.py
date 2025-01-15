import yaml

requiredConstants: set[str] = {"THMP_E", "FEJIO_A"}

def writeRequiredConstantsToFile() -> None:
    with open("config.yaml", "w+") as f:
        data_to_write = {}
        constants = data_to_write["constants"]
        
        for constant in requiredConstants:
            constants.append(constant)