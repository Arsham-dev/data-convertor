import json
from dicttoxml import dicttoxml

def json_to_xml(json_file_path:str):
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    xml_data = dicttoxml(data, custom_root='root', attr_type=False)

    with open(json_file_path.replace(".json", ".xml"), "wb") as xml_file:
        xml_file.write(xml_data)
