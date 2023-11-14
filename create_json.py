import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __repr__(self):
        return f"{self.name}, {self.dob}, {self.height}, {self.city}, {self.state}"


employee_data = [
    {"name": "surya", "dob": "04/04/1997", "height": "6'0", "city": "Chittoor", "state": "AP"},
    {"name": "saravana", "dob": "02/02/1998", "height": "5'6", "city": "Tirupati", "state": "AP"},
    {"name": "gokul", "dob": "03/03/2000", "height": "6'2", "city": "Vellore", "state": "TN"},
    {"name": "hari", "dob": "04/04/1996", "height": "5'5", "city": "Chennai", "state": "TN"},
    {"name": "sathish", "dob": "05/05/1997", "height": "6'1", "city": "selam", "state": "AP"},
]

with open("employee.json", "w") as file:
    json.dump(employee_data, file)

# read the employee information from the JSON file
employee_objects = []
with open("employee.json", "r") as file:
    employee_data = json.load(file)
    for employee in employee_data:
        employee_objects.append(
            Employee(
                name=employee["name"],
                dob=employee["dob"],
                height=employee["height"],
                city=employee["city"],
                state=employee["state"],
            )
        )

# print the list of employee objects
print(employee_objects)
