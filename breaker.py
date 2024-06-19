
import os.path
import re

def process(msgtype, msgname):
    """
    Process a ROS message type and its corresponding instance name.
    
    """

    
    filename = os.path.join(os.path.dirname(__file__), "Messages", f"{msgtype}.msg")
    return parse_msg_file(msgtype, filename, msgname, [])

def parse_msg_file(name, filename, msgname, output):
    """
    Parse the Messages/ directory and return the structure of the message. 

    """
    
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if not line.startswith("#") and line:
            parts = line.split()
            field_type = parts[0]
            field_name = parts[1]
            array_match = re.match(r"(.+?)\[(\d*)\]", field_type)
            if array_match:
                base_type = array_match.group(1)
                array_size = array_match.group(2)
                array_size = int(array_size) if array_size else "unspecified"
                field_type = base_type
            if (field_type.__contains__("/")):
                field_type = field_type.split("/")[1]
            if not is_primative(field_type):
                nested_filename = os.path.join(os.path.dirname(__file__), "Messages", f"{field_type}.msg")
                parse_msg_file(name, nested_filename, f"{msgname}.{field_name}", output)
            else:
                output.append(f"{msgname}.{field_name}")
    return output

def is_primative(field_type):
    """
    Check if the type of a field is a ROS primitive date type.
    
    """

    primitive_types = {"int8", "uint8", "int16", "uint16", "int32", "uint32", "int64", "uint64", "float32", "float64", "bool", "string", "time", "duration", "byte"}
    return field_type in primitive_types
