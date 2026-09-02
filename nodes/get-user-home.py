# prepare interface
from pathlib import Path

NODE_ID = "GetUserHome"
NODE_NAME = "Get User Home"
NODE_CATEGORY = "OS Utils"
NODE_DESCRIPTION = (
    "This node returns simply the Users home directory"
)

PARAMETERS = [
]

INPUTS = [{"name": "input0", "label": "Input", "type": "any"}]
OUTPUTS = [
    {"name": "output0", "label": "User Home", "type": "string", "identifier": "home"}
]


def execute(config, inputs, secrets):
    # get parameters
    

    # functionality
    home = str(Path.home()).replace("\\", "/")
    
    
    # return result
    return {
        "status": "success",
        "message": "User Home",
        "output_data": {
            "output0": {"identifier": "result", "type": "string", "value": home}
        },
    }
