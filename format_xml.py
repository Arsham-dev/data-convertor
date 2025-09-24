from xml.dom.minidom import parseString

def format_xml(xml_string:str):
    with open(xml_string, "r") as file:
        xml_content = file.read()

    dom = parseString(xml_content)
    pretty_xml = dom.toprettyxml(indent="  ") 

    with open("formatted.xml", "w") as file:
        file.write(pretty_xml)

