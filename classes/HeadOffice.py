from .Office import Office


class HeadOffice(Office):

    def __init__(self, branchId, branchAddress, branchPhone, numberOfTrucks, numberOfEmployees, volumeHandled, revenueGenerated, idleWaitingTime, rate):
        super().__init__(branchId, branchAddress, branchPhone, numberOfTrucks,
                         numberOfEmployees, volumeHandled, revenueGenerated, idleWaitingTime, rate)
        self.isHead = True
