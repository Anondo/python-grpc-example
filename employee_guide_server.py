import grpc
import time
import employee_guide_resources
from concurrent import futures
from generated import employee_guide_pb2
from generated import employee_guide_pb2_grpc

class EmployeeGuideServicer(employee_guide_pb2_grpc.EmployeeGuideServicer):

    def __init__(self):
        self.employees = employee_guide_resources.read_employee_guide_data()

    def get_employee(self , id = None):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def GetOneEmployee(self , request , context):
        employee = self.get_employee(request)
        if not employee:
            return employee_guide_pb2.Employee(id = request , name = "" ,
            designation = "" , salary = 0)
        return employee
    def GetEmployees(self , request , context):
        for employee in self.employees:
            yield employee
    def putEmployee(self , request , context):
        employee_guide_resources.add_employee_guide_data(
            name = request.name,
            designation = request.designation,
            salary = request.salary
        )
        return employee_guide_pb2.Log(msg="Employee Entry Successful")
    def deleteEmployee(self , request , context):
        employee_guide_resources.delete_employee_guide_data(request.number)
        return employee_guide_pb2.Log(msg="Employee deletion Successful")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    employee_guide_pb2_grpc.add_EmployeeGuideServicer_to_server(
    EmployeeGuideServicer() , server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        print("gRPC server is running... ... ... ...")
        time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
