from .Customer import Customer


class Sender(Customer):
    def __init__(self, customerName, customerAddress, customerMobile, customerEmailId, customerId, customerConsignmentId):
        super().__init__(customerName, customerAddress, customerMobile,
                         customerEmailId, customerId, customerConsignmentId)
        self.DispatchStatus = False
