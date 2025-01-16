import yaml
import os
from enum import Enum
from dataclasses import dataclass
import inspect
from typing import Any

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

    configData[scriptname][constant] = 0

    writeRequiredConstantsToFile()

def writeRequiredConstantsToFile() -> None:
    # Read from file
    with open("config.yml", "r") as f:
        data = yaml.safe_load(f)

        if data != None: 
            for loadedScriptname, loadedConstants in data.items():
                for loadedName, loadedValue in loadedConstants.items():
                    if not loadedScriptname in configData:
                        configData[loadedScriptname] = {}

                    configData[loadedScriptname][loadedName] = loadedValue

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
    scriptname = getNameOfCallBehaviour()

    if not scriptname in configData:
        raise KeyError(f"Scriptname {scriptname} cannot be found in {configData}")

    return configData[scriptname][name]

writeRequiredConstantsToFile()

