import json

student = {
    "id": 1,
    "name": "Adesina Tinubu",
    "gender": "Male",
    "department": "Mathematic Science",
    "school": "University of Osun"
}

with open("013_data.json", "w") as json_file:
          json.dump(student, json_file, indent=4)
        
