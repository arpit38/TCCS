import datetime


class Office:
    rate = 0

    def __init__(self, branchId, branchAddress, branchPhone, numberOfTrucks, numberOfEmployees, volumeHandled, revenueGenerated, idleWaitingTime, rate):
        self.BranchId = branchId
        self.BranchAddress = branchAddress
        self.BranchPhone = branchPhone
        self.NumberOfTrucks = numberOfTrucks
        self.NumberOfEmployees = numberOfEmployees
        self.VolumeHandled = volumeHandled
        self.RevenueGenerated = revenueGenerated
        self.IdleWaitingTime = idleWaitingTime
        Office.rate = rate

    def toString(self):
        # avg = self.IdleWaitingTime
        # rez = str(avg/3600) + ' ' + str((avg % 3600)/60) + ' ' + str(avg % 60)
        # time = rez
        data = f'BranchId: {self.BranchId}\nBranch Address: {self.BranchAddress}\n'
        data = data+f"Branch Phone: {self.BranchPhone}\n"
        data = data+f"Number of Trucks: {self.NumberOfTrucks}\n"
        data = data+f"Number Of Employees: {self.NumberOfEmployees}\n"
        data = data+f"Volume Handled: {self.VolumeHandled}\n"
        data = data + \
            f"Averaged Truck idle Waiting Time: {self.IdleWaitingTime}\n"
        return data

    def raw(self):
        data = ""
        idle = f"{self.IdleWaitingTime}"
        idle = idle.split('.')[0]
        data = f'{self.BranchId};{self.BranchAddress};'
        data = data+f"{self.BranchPhone};"
        data = data+f"{self.NumberOfTrucks};"
        data = data+f"{self.NumberOfEmployees};"
        data = data+f"{self.VolumeHandled};"
        data = data+f"{self.RevenueGenerated};"
        data = data+f"{idle};"
        data = data+f"{Office.rate}"
        return data
