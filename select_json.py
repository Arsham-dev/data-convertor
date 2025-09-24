import json

def select_json(labels:str,file:str):
    label_items = labels.split(",")
    with open(file, "r") as json_file:
        data = json.load(json_file)
    new_data = []
    for item in data:
        raw={}
        for label in label_items:
            print(label)
            raw[label] = item[label]
        new_data.append(raw)
        
    with open("students-new.json", "w", encoding="utf-8") as out:
        json.dump(new_data, out, ensure_ascii=False, indent=2)
    
select_json("StudentNumber,NationalCode,FirstName,LastName,StartDate,TermEndDate,DormitoryCode,DormitoryName,RoomNumber,DormitoryStatusName","students.json")