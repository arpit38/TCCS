class Consignment:
    def __init__(self, volume, sender, receiver, revenueGenerated, isTruckAssigned, truckAssigned, dispatechedAndReceived, sourcebranch, destinationBranch, consignmentId):
        self.volume = volume
        self.sender = sender
        self.receiver = receiver
        self.revenueGenerated = revenueGenerated
        self.isTruckAssigned = isTruckAssigned
        self.truckAssigned = truckAssigned
        self.dispatechedAndReceived = dispatechedAndReceived
        self.sourcebranch = sourcebranch
        self.destinationBranch = destinationBranch
        self.consignmentId = consignmentId

    def toString(self):
        data = ""
        data = data+f"Consignment id: {self.consignmentId}\n"
        data = data+f"Consignment volume: {self.volume}\n"
        data = data+f"Consignment sender id: {self.sender.CustomerId}\n"
        data = data+f"Consignment sender Name: {self.sender.CustomerName}\n"
        data = data+f"Consignment receiver id: {self.receiver.CustomerId}\n"
        data = data + \
            f"Consignment receiver Name: {self.receiver.CustomerName}\n"
        data = data+f"Consignment revenue Generated: {self.revenueGenerated}\n"
        data = data+f"is Truck Assigned: {self.isTruckAssigned}\n"
        data = data + \
            f"Truck Assignned id: {self.truckAssigned if not self.truckAssigned==-1 else 'None'  }\n"
        data = data + \
            f"Consignment Status: {self.dispatechedAndReceived}\n"
        data = data + \
            f"Consignment source branch id: {self.sourcebranch.BranchId}\n"
        data = data + \
            f"Consignment source branch Address: {self.sourcebranch.BranchAddress}\n"
        data = data + \
            f"Consignment destination Branch id: {self.destinationBranch.BranchId}\n"
        data = data + \
            f"Consignment destination Branch Address: {self.destinationBranch.BranchAddress}\n"
        return data

    def raw(self):
        r = self.receiver.raw()
        data = ""
        s = self.sender.raw()
        data = data+f'{self.volume};'
        data = data+f'{s};'
        data = data+f'{r};'
        data = data+f'{self.revenueGenerated};'
        data = data+f'{self.isTruckAssigned};'
        data = data+f'{self.truckAssigned};'
        data = data+f'{self.dispatechedAndReceived};'
        data = data+f'{self.sourcebranch.BranchId};'
        data = data+f'{self.destinationBranch.BranchId};'
        data = data+f'{self.consignmentId}'
        return data
