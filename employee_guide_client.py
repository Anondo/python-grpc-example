import grpc
from generated import employee_guide_pb2
from generated import employee_guide_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")



def get_one_employee(stub , id):
    employee = stub.GetOneEmployee(id)

    if not employee.id or not employee.name:
        print("Data could not be served properly!!")
    print (employee)

def get_employees(stub):
    for employee in stub.GetEmployees(employee_guide_pb2.ID(number=-1)):
        print(employee)

def put_employee(stub , employee):
    print(stub.putEmployee(employee))

def delete_employee(stub , id):
    print(stub.deleteEmployee(id))

def run():
    stub = employee_guide_pb2_grpc.EmployeeGuideStub(channel)
    id = employee_guide_pb2.ID(number = 1)
    get_one_employee(stub, id)
    get_employees(stub)
    #put_employee(stub , employee_guide_pb2.Employee(name="Anondo",designation=
    #{}"Intern Tech" , salary=5000))
    delete_employee(stub , employee_guide_pb2.ID(number=4))


if __name__ == '__main__':
    run()
