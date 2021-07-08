from .Employee import Employee


class Manager(Employee):
    def __init__(self, employeeName, employeeId, employeeAddress, employeeMobileNo, employeeEmailId, employeeBranchId, empPassword):
        super().__init__(employeeName, employeeId, employeeAddress,
                         employeeMobileNo, employeeEmailId, employeeBranchId, empPassword)

        self.isManager = True
