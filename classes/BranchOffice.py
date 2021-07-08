from .Office import Office


class BranchOffice(Office):

    def __init__(self, branchId, branchAddress, branchPhone, numberOfTrucks, numberOfEmployees, volumeHandled, revenueGenerated, idleWaitingTime, rate):
        super().__init__(branchId, branchAddress, branchPhone, numberOfTrucks,
                         numberOfEmployees, volumeHandled, revenueGenerated, idleWaitingTime, rate)
        self.isBranch = True
