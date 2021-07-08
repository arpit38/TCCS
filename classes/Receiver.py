from .Customer import Customer


class Receiver(Customer):
    def __init__(self, customerName, customerAddress, customerMobile, customerEmailId, customerId, customerConsignmentId):
        super().__init__(customerName, customerAddress, customerMobile,
                         customerEmailId, customerId, customerConsignmentId)
        self.ReceivedStatus = False
