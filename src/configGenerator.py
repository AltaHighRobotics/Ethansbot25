import yaml
import os
import inspect
from typing import Any
from wpilib.shuffleboard import Shuffleboard

configData = {}

def getNameOfCallBehaviour() -> str:
    filename = inspect.stack()[2].filename    
    if filename == None:
        raise RuntimeError("Some weird file shit idk")

    filenameWithoutDotPy = os.path.basename(filename).split(".")[0]
    return filenameWithoutDotPy

def requireConfigConstant(constant: str, scriptname: str = ""):
    if scriptname == "":
        scriptname = getNameOfCallBehaviour()

    if not scriptname in configData:
        configData[scriptname] = {}


    tab = Shuffleboard.getTab(scriptname)
    entry = tab.add(constant, 0.0).getEntry()
    print(dir(entry))
    configData[scriptname][constant] = entry

def load() -> None:
    with open("config.yml", "r") as f:
        data = yaml.safe_load(f)

        if data != None: 
            for loadedScriptname, loadedConstants in data.items():
                for loadedName, loadedValue in loadedConstants.items():
                    if not loadedScriptname in configData:
                        configData[loadedScriptname] = {}

                    configData[loadedScriptname][loadedName] = loadedValue


def writeRequiredConstantsToFile() -> None:
    # Read from file
    # Write to file
    with open("config.yml", "w+") as f:
        yaml.dump(configData, f, default_flow_style=False)

    # Add fancy new lines
    yaml_output = ""
    with open("config.yml", "r") as f:
        yaml_output = f.read()
    with open("config.yml", "w+") as f:
        f.write('\n'.join([line if line == '' or line.startswith(' ') else '\n' + line for line in yaml_output.splitlines()]))

def cget(name: str):
    def getValue(entry):
        return entry.getFloat(0.0)

    scriptname = getNameOfCallBehaviour()

    if not scriptname in configData:
        raise KeyError(f"Scriptname {scriptname} cannot be found in {configData}")

    return getValue(configData[scriptname][name])

