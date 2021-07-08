class Truck:
    def __init__(self, truckNo, currentBranch, numberOfConsignmentsHandled, status, usage):

        self.truckNo = truckNo
        self.currentBranch = currentBranch
        self.numberOfConsignmentsHandled = numberOfConsignmentsHandled
        self.status = status
        self.usage = usage

    def toString(self):
        status = ""
        if self.status == 0:
            status = 'Free'
        if self.status == 1:
            status = 'Loading Consginments'
        data = f"Truck No:{self.truckNo}\nNumber of Consignments: {self.numberOfConsignmentsHandled}\nCurrent Brach: {self.currentBranch}\nStatus: {status}\nCurrent Volume Loaded: {self.usage}"
        return data

    def raw(self):
        data = ""
        data = data+f"{self.truckNo};"
        data = data+f"{self.currentBranch};"
        data = data+f"{self.numberOfConsignmentsHandled};"
        data = data+f"{self.status};"
        data = data+f"{self.usage}"
        return data
