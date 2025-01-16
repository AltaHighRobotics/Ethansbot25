import yaml
import os
from enum import Enum
from dataclasses import dataclass
import inspect

@dataclass
class Constant:
    constantName: str
    scriptname: str

requiredConstants: list[Constant] = []

def requireConfigConstant(constant):
    print("GOGJIOEWIOFIOEWJIFWEJIOJIO")
    if type(constant) == Constant:
        requiredConstants.append(constant)
    elif type(constant) == str:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        filename = os.path.basename(filename).split(".")[0]
        requiredConstants.append(Constant(constant, filename))
    else:
        raise TypeError("Not a valid argument")

def writeRequiredConstantsToFile() -> None:
    all_constant_names: list[str] = []
    all_constants = requiredConstants

    # Read from file
    with open("config.yml", "r") as f:
        data = yaml.safe_load(f)
        constantsYml = data["constants"]

        def readFromFile():
            if constantsYml == None:
                return
            for scriptname, scriptConstants in constantsYml.items():
                for constantName, value in scriptConstants.items():
                    all_constants.append(Constant(constantName, scriptname))
                    print(f"Read {constantName}")
        
        readFromFile()


    # Write to file
    with open("config.yml", "w+") as f:
        data_to_write = {"constants": {}}
        constantsYml = data_to_write["constants"]

        for constant in requiredConstants:
            if not constant.scriptname in constantsYml:
                constantsYml[constant.scriptname] = {}

            constantsYml[constant.scriptname][constant.constantName] = 0
            print(f"Write {constant.constantName}")

        yaml.dump(data_to_write, f, default_flow_style=False)


