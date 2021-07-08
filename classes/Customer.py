class Customer:
    def __init__(self,  customerName,   customerAddress,   customerMobile,   customerEmailId,
                 customerId,   customerConsignmentId):
        self.CustomerName = customerName
        self.CustomerAddress = customerAddress
        self.CustomerMobile = customerMobile
        self.CustomerEmailId = customerEmailId
        self.CustomerId = customerId
        self.CustomerConsignmentId = customerConsignmentId

    def raw(self):
        data = ""
        data = data+f"{self.CustomerName};"
        data = data+f"{self.CustomerAddress};"
        data = data+f"{self.CustomerMobile};"
        data = data+f"{self.CustomerEmailId};"
        data = data+f"{self.CustomerId};"
        data = data+f"{self.CustomerConsignmentId}"
        return data

    def toString(self):
        return "Customer [CustomerName=" + CustomerName + ", CustomerAddress=" + CustomerAddress + ", CustomerMobile="
        + CustomerMobile + ", CustomerEmailId=" + \
            CustomerEmailId + ", CustomerId=" + CustomerId
        + ", CustomerConsignmentId=" + CustomerConsignmentId + "]"
