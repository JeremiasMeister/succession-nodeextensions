NODE_ID = "ToForwardSlash"
NODE_NAME = "To Forward Slash"
NODE_CATEGORY = "OS Utils"
NODE_DESCRIPTION = (
    "This node converts all occurances of \ to / in a string"
)

PARAMETERS = [
    {
        "name": "path",
        "label": "Path",
        "type": "string"
    }
]

INPUTS = [{"name": "input0", "label": "Input", "type": "any"}]
OUTPUTS = [
    {"name": "output0", "label": "Path", "type": "string", "identifier": "path"}
]


def execute(config, inputs, secrets):
    # get parameters
    path = config.get("path")
    if not path:
        path = ""
    

    # functionality
    result = str(path).replace("\\", "/")
    
    
    # return result
    return {
        "status": "success",
        "message": "User Home",
        "output_data": {
            "output0": {"identifier": "result", "type": "string", "value": result}
        },
    }
