# Project Succession expects a few constants to properly handle the node code. they are defined below

# Begin constants
NODE_ID = "ThresholdCompare"
NODE_NAME = "Threshold Compare"
NODE_CATEGORY = "Utils"
NODE_DESCRIPTION = "Compares if one float value deviates from another within a threshold"

INPUTS = [{"name": "input0", "label": "Input", "type": "any"}]
OUTPUTS = [
    {"name": "output0", "label": "In Threshold", "type": "any", "identifier": "passthrough_data"},
    {"name": "output1", "label": "Out of Threshold", "type": "any", "identifier": "passthrough_data"},
]

PARAMETERS = [
    {
        "name": "compare",
        "label": "Data to Compare",
        "type": "float",
        "defaultValue": 1.0,
        "required": True
    },
    {
        "name": "method",
        "label": "Method",
        "type": "enum",
        "options": ["BothDirections", "SmallerOnly", "BiggerOnly"],
        "defaultValue": "BothDirections",
        "required": True
    },
    {
        "name": "threshold",
        "label": "Threshold",
        "defaultValue": 0.1,
        "type": "float"
    },
    {
        "name": "compare_with",
        "label": "Data to Compare with",
        "type": "float",
        "defaultValue": 1.0,
        "required": True
    },
]
# end constants

# Project Succession requires this execute method to be present. it defines the functionality of the nodes. 
def execute(config, inputs, secrets):
    # get params
    compare = config.get("compare")
    compare_with = config.get("compare_with")
    method = config.get("method")
    threshold = config.get("threshold")
    
    output = "output0"
    if method == "SmallerOnly":
        cvalue = compare_with - threshold
        if compare < cvalue:
            output = "output1"
    elif method == "BiggerOnly":
        cvalue = compare_with + threshold
        if compare > cvalue:
            output = "output1"
    else:
        cvalue1 = compare_with - threshold
        cvalue2 = compare_with + threshold
        if compare < cvalue1 or compare > cvalue2:
            output = "output1"

    # The return struct is properly structured into status, message and output_data which contains proper identifier, type and value for each output.
    # optionally we can limit the outputs firing with the firing_outputs field
    return {
        "status": "success",
        "message": "Threshold Compare Output",
        "output_data": {
            "output0": {"identifier": "passthrough_data", "type": "any", "value": inputs.get("input0")},
            "output1": {"identifier": "passthrough_data", "type": "any", "value": inputs.get("input0")}
        },
        "firing_outputs": [output]
    }
