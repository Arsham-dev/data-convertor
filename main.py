import argparse
from html_to_json import html_to_json 
from format_xml import format_xml
from json_to_xml import json_to_xml
def main():
    parser = argparse.ArgumentParser(description="CLI tool for XML/HTML/JSON conversions")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # format-xml
    parser_xml = subparsers.add_parser("format-xml", help="Format an XML file")
    parser_xml.add_argument("xml_file", help="Path to the XML file")

    # html-to-json
    parser_html = subparsers.add_parser("html-to-json", help="Convert HTML to JSON")
    parser_html.add_argument("html_file", help="Path to the HTML file")
    parser_html.add_argument("tag", help="HTML tag to extract")

    # json-to-xml
    parser_json = subparsers.add_parser("json-to-xml", help="Convert JSON to XML")
    parser_json.add_argument("json_file", help="Path to the JSON file")

    args = parser.parse_args()

    if args.command == "format-xml":
        format_xml(args.xml_file)
    elif args.command == "html-to-json":
        print(args.tag)
        html_to_json(args.html_file, args.tag)
    elif args.command == "json-to-xml":
        json_to_xml(args.json_file)


if __name__ == "__main__":
    main()