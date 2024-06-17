import os
import re
output_lines=[]
def parse_msg_file(name,filename):
    f=open(filename, 'r')
    lines = f.readlines()

    types = []
    
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
            
            
            if(field_type.__contains__("/")):
                field_type=field_type.split("/")[1]

            if not is_primitive(field_type):
                nested_filename = os.path.join(os.path.dirname(__file__), f"{field_type}.msg")
                
                parse_msg_file(name+"."+field_name,nested_filename)
            else:
                
                output_line = f"list.append({name}.{field_name})"
                output_lines.append(output_line)
                
                

            types.append(field_type)
            

    return output_lines

def is_primitive(field_type):
    primitive_types = {'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64',
                       'float32', 'float64', 'bool', 'string', 'time', 'duration'}
    return field_type in primitive_types

def process(input_message):
    
    
    filename = os.path.join("D://Users//vikha//Downloads//Vbox shared//Code//destination", f"{input_message}.msg")
    return parse_msg_file(input_message,filename)


