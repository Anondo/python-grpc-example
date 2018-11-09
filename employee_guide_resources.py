
import json
from generated import employee_guide_pb2

def read_employee_guide_data():
    employees = []


    with open("resources/employee_guide.json") as emp_file:
        for data in json.load(emp_file):
            id = data["id"]["number"]
            name = data["name"]
            designation = data["designation"]
            salary = data["salary"]
            employees.append(employee_guide_pb2.Employee(
            id = employee_guide_pb2.ID(number=id), name = name,
            designation = designation , salary = salary)
            )
    return employees


def delete_employee_guide_data(id):
    with open("resources/employee_guide.json") as emp_file:
        employees = []
        for data in json.load(emp_file):
            if data["id"]["number"] == id:
                continue
            employees.append(data)
        _writeData(json.dumps(employees ,indent=4 ,  separators=(',',':')))


def add_employee_guide_data(name = "" , designation = "" , salary = 0):
    with open("resources/employee_guide.json" , mode='r') as emp_file:
        data = json.load(emp_file)
        id = len(data) + 1
        entry = {"id":{"number":id},"name":name ,
        "designation":designation, "salary":salary}
        data.append(entry)
        _writeData(json.dumps(data ,indent=4 ,  separators=(',',':')))
def _writeData(data):
    with open("resources/employee_guide.json" , mode='w') as emp_file:
        emp_file.write(data)
