from bs4 import BeautifulSoup
import json
import re

def to_camel_case(s: str) -> str:
    s = s.lower()
    parts = re.split(r'[_\s]+', s)
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def html_to_json(html_file:str,tag:str):
    with open(html_file, "r", encoding="utf-8") as f:
        html_data = f.read()

    soup = BeautifulSoup(html_data, "html.parser")

    p_tags = soup.find_all(tag)

    students = []
    for p in p_tags:
        student_data = {}
        for attr, value in p.attrs.items():
            key = (attr)  
            student_data[key] = value.strip()
        students.append(student_data)

    with open(html_file.replace(".html", ".json"), "w", encoding="utf-8") as out:
        json.dump(students, out, ensure_ascii=False, indent=2)