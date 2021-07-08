class Employee:
    def __init__(self, employeeName, employeeId, employeeAddress, employeeMobileNo, employeeEmailId, employeeBranchId, empPassword):
        self.EmployeeName = employeeName
        self.EmployeeId = employeeId
        self.EmployeeAddress = employeeAddress
        self.EmployeeMobileNo = employeeMobileNo
        self.EmployeeEmailId = employeeEmailId
        self.EmployeeBranchId = employeeBranchId
        self.EmpPassword = empPassword

    def toString(self):
        data = ""
        data = data+f"EmployeeId: {self.EmployeeId}\n"
        data = data+f"Employee Name: {self.EmployeeName}\n"
        data = data+f"Employee Address: {self.EmployeeAddress}\n"
        data = data+f"Employee Mobile No: {self.EmployeeMobileNo}\n"
        data = data+f"Employee EmailId: {self.EmployeeEmailId}\n"
        data = data+f"Employee BranchId: {self.EmployeeBranchId}\n"
        data = data+f"Employee Password: {self.EmpPassword}\n"
        return data

    def raw(self):
        data = ""
        data = data+f"{self.EmployeeId};"
        data = data+f"{self.EmployeeName};"
        data = data+f"{self.EmployeeAddress};"
        data = data+f"{self.EmployeeMobileNo};"
        data = data+f"{self.EmployeeEmailId};"
        data = data+f"{self.EmployeeBranchId};"
        data = data+f"{self.EmpPassword}"
        return data
