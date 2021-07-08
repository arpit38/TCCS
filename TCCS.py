from classes.Manager import Manager
from classes.HeadOffice import HeadOffice
from classes.BranchOffice import BranchOffice
from classes.Employee import Employee
from classes.Truck import Truck
from classes.Office import Office
from classes.Sender import Sender
from classes.Receiver import Receiver
from classes.Consignment import Consignment
import datetime
import json
rate = 30
headOffice = HeadOffice(0, 'address', '03xxxxxxxx', 0,
                        0, 0, 0, datetime.timedelta(), rate)
branches = [headOffice]
headManager = Manager('head', 0, 'addr', '00303', '1', 0, '1')

employees = []
trucks = []
consignments = []
laod = []
recievers = []
senders = []
truck_usage = []


def save_head():
    f = open('head.txt', 'w')
    data = headManager.raw()
    f.write(data)


def save_branches():
    f = open('office.txt', 'w')
    f.truncate()
    for b in branches:
        f.write(b.raw())
        f.write('\n')


def save_trucks():
    f = open('trucks.txt', 'w')
    f.truncate()
    for t in trucks:
        f.write(t[0].raw())
        f.write(";")
        f.write(str(t[1].timestamp()))
        f.write(";")
        f.write(str(t[2]))
        f.write('\n')


def load_trucks():
    f = open('trucks.txt', 'r')
    for line in f:
        data = line.split(';')
        tr = Truck(int(data[0]), int(data[1]), int(
            data[2]), int(data[3]), int(data[4]))
        time = float(data[5])
        time = datetime.datetime.fromtimestamp(time)
        des = int(data[6])
        t = [tr, time, des]
        trucks.append(t)


def save_consignments():
    f = open('consignments.txt', 'w')
    f.truncate()
    for c in consignments:
        f.write(c[0].raw())
        f.write(";")
        f.write(str(datetime.datetime.strftime(c[1], "%H:%M:%S")))
        f.write(";")
        f.write(str(datetime.datetime.strftime(c[2], "%H:%M:%S")))
        f.write(';\n')


def load_consignments():
    f = open('consignments.txt', 'r')
    for line in f:
        data = line.split(';')
        v = float(data[0])
        s = Sender(data[1], data[2], data[3], data[4],
                   int(data[5]), int(data[6]))
        r = Receiver(data[7], data[8], data[9], data[10],
                     int(data[11]), int(data[12]))
        sb = None
        db = None
        sid = int(data[17])
        did = int(data[18])
        for b in branches:
            if b.BranchId == sid:
                sb = b
            if b.BranchId == did:
                db = b
        c = Consignment(v, s, r, int(data[13]), bool(data[14]), int(
            data[15]), data[16], sb, db, int(data[19]))
        t1 = data[20]
        t1 = t1.split('.')[0]
        t2 = data[21]
        t2 = t2.split('.')[0]
        t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
        t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
        print(t2)
        consignments.append([c, t1, t2])


def load_branches():
    f = open('office.txt', 'r')
    branches.pop()
    for line in f:
        data = line.split(";")
        d = data[7]
        t = datetime.datetime.strptime(d, "%H:%M:%S")
        # ...and use datetime's hour, min and sec properties to build a timedelta
        delta = datetime.timedelta(
            hours=t.hour, minutes=t.minute, seconds=t.second)
        b = BranchOffice(int(data[0]), data[1], data[2], int(data[3]), int(data[4]), int(
            data[5]), float(data[6]), delta, int(data[8]))
        branches.append(b)


def load_head():
    f = open('head.txt', 'r')
    data = f.readline()
    data = data.split(';')
    headManager.EmployeeName = data[1]
    headManager.EmployeeId = int(data[0])
    headManager.EmployeeAddress = data[2]
    headManager.EmployeeMobileNo = data[3]
    headManager.EmployeeEmailId = data[4]
    headManager.EmployeeBranchId = int(data[5])
    headManager.EmpPassword = data[6]


def save_to_file():
    save_head()
    save_branches()
    save_trucks()
    save_consignments()
    return


def laod_from_file():
    load_head()
    load_branches()
    load_trucks()
    load_consignments()


def add_branch_handler():
    id = input("Enter Branch id:")
    id = int(id)
    addr = input("Enter Address: ")
    phone = input("Enter Phone: ")
    if id not in [b.BranchId for b in branches]:
        branch = BranchOffice(id, addr, phone, 0, 0, 0, 0,
                              datetime.timedelta(), Office.rate)
        branches.append(branch)
        print("Branch added successfully")
    else:
        print("Branch Already Exists...")


def add_employee_handler():
    id = input("Enter Employee Id: ")
    id = int(id)
    name = input("Enter Employee Name: ")
    addr = input("Enter Employee Address: ")
    phone = input("Enter Employee Mobile Number: ")
    email = input("Enter Employee Email: ")
    password = input("Enter Employee Password: ")
    print("Branchs:")
    for b in branches:
        print("Branch Id: ", b.BranchId)
    bid = input("Enter Branch Id: ")
    bid = int(bid)
    if id not in [emp.EmployeeId for emp in employees] and bid in [b.BranchId for b in branches]:
        e = Employee(name, id, addr, phone, email, bid, password)
        employees.append(e)
        for b in branches:
            if b.BranchId == bid:
                b.NumberOfEmployees = b.NumberOfEmployees+1
        print("Employee Added Successfully")
    else:
        print("Invalid Input")


def check_full(t):
    if t[0].usage >= 500:
        time = datetime.datetime.now()
        tu = (t[0].truckNo, t[0].numberOfConsignmentsHandled,
              t[0].currentBranch, t[2], time-t[1], time)
        t[0].status = 0
        t[0].usage = 0
        t[0].numberOfConsignmentsHandled = 0
        for c in consignments:
            if c[0].dispatechedAndReceived != "Completed" and c[0].sourcebranch.BranchId == t[0].currentBranch and c[0].destinationBranch.BranchId == t[2]:
                c[0].isTruckAssigned = False
                c[0].dispatechedAndReceived = 'Completed'
                c[2] = datetime.datetime.now()
                avg = c[0].sourcebranch.IdleWaitingTime
                current = datetime.datetime.now()-t[1]
                avg = current-avg
                avg = avg/c[0].sourcebranch.NumberOfTrucks
                c[0].sourcebranch.IdleWaitingTime = c[0].sourcebranch.IdleWaitingTime+avg
                c[0].sourcebranch.NumberOfTrucks = c[0].sourcebranch.NumberOfTrucks-1
                c[0].sourcebranch.VolumeHandled = c[0].sourcebranch.VolumeHandled+c[0].volume
                c[0].sourcebranch.RevenueGenerated = c[0].sourcebranch.RevenueGenerated + \
                    c[0].revenueGenerated
                c[0].destinationBranch.NumberOfTrucks = c[0].destinationBranch.NumberOfTrucks+1
                t[0].currentBranch = c[0].destinationBranch.BranchId
                print("---------Consignmenst Transferred-----------")
                print(c[0].toString())
        t[1] = datetime.datetime.now()


def add_truck_handler():
    tno = input("Enter Truch Number: ")
    print("Branches:")
    for b in branches:
        print("Branch ID: ", b.BranchId)
    cb = input("Enter Branch id:")
    cb = int(cb)
    if tno not in [t[0].truckNo for t in trucks] and cb in [b.BranchId for b in branches]:
        tr = Truck(tno, cb, 0, 0, 0)
        t = [tr, datetime.datetime.now(), -1]
        trucks.append(t)
        for b in branches:
            if b.BranchId == cb:
                b.NumberOfTrucks = b.NumberOfTrucks+1
        check_full(t)
        print("Truck added Succesfully")
    else:
        print("Invalid Input")


def view_employees():
    for emp in employees:
        print(emp.toString())


def view_trucks():
    print("----------Trucks data-------------")
    for tr in trucks:
        print(tr[0].toString())
        print('\n')


def allot_truck(consignment):
    for t in trucks:
        if t[0].currentBranch == consignment.sourcebranch.BranchId:
            consignment.truckAssigned = t[0].truckNo
            consignment.isTruckAssigned = True
            t[0].numberOfConsignmentsHandled = t[0].numberOfConsignmentsHandled+1
            t[0].usage = t[0].usage+consignment.volume
            t[0].status = 1
            t[2] = consignment.destinationBranch.BranchId
            check_full(t)
            break


def view_branches():
    print("----------Branches data-------------\n")
    for b in branches:
        print(b.toString())


def view_all_consignments():
    for cons in consignments:
        print("-----------Consignment---------------")
        print(cons[0].toString())
        time = datetime.datetime.now()
        if cons[0].dispatechedAndReceived != 'Completed':
            print("Waiting Time:", time-cons[1])
        else:
            print("Waiting Time:", cons[2]-cons[1])


def view_consignments(cb):
    for cons in consignments:
        print("---------------Consignment-----------------")
        if cons[0].sourcebranch.BranchId == cb:
            print(cons[0].toString())
            time = datetime.datetime.now()
            if cons[0].dispatechedAndReceived != 'Completed':
                t = time-cons[1]
                print("Waiting Time:", t)
            else:
                print("Waiting Time:", cons[2]-cons[1])


def check_available_truck(cb):
    for i in range(len(trucks)):
        if trucks[i].currentBranch == cb:
            return trucks[i].truckNo
    return -1


def view_truck_usage():
    print("------Truck Usage History--------")
    for tu in truck_usage:
        print("Truck No: ", tu[0])
        print("Number of Consignments: ", tu[1])
        print("Source Branch: ", tu[2])
        print("Destination Branch: ", tu[3])
        print("Wait Time: ", tu[4])
        print("Tiem of Travel: ", tu[5])


def add_consignment_handler(cb):
    print("------------Add Consignment-------------")
    print("Sender Details: ")
    sid = input("Enter Sender ID: ")
    sid = int(sid)
    sname = input("sender name:")
    saddr = input("Enter Sender Address: ")
    smobile = input("Enter Sender mobile number: ")
    semail = input("Enter Sender Address: ")
    print("Receiver Details: ")
    rid = input("Enter Receiver ID: ")
    rid = int(rid)
    rname = input("Enter Receiver name:")
    raddr = input("Enter Receiver Address: ")
    rmobile = input("Enter Receiver mobile number: ")
    remail = input("Enter Receiver Email Address: ")
    print("Consignment Details:")
    cid = input("Consignment id:")
    cid = int(cid)
    if cid in [c[0].consignmentId for c in consignments]:
        print("Invalid COnsignment Id")
        return
    cv = input("volume:")
    cv = int(cv)
    sb = cb
    print("Branches: ")
    for b in branches:
        print("Brach Id: ", b.BranchId)
    db = input("destination branch:")
    db = int(db)
    if db not in [b.BranchId for b in branches]:
        print("Invalid Destination Branch Id")
        return
    source = None
    des = None
    for b in branches:
        if b.BranchId == sb:
            source = b
        if b.BranchId == db:
            des = b
    revenue = Office.rate*cv
    r = Receiver(rname, raddr, rmobile, remail, rid, cid)
    s = Sender(sname, saddr, smobile, semail, sid, cid)
    c = Consignment(cv, s, r, revenue, False, -1, 'Waiting', source, des, cid)
    # print(c.__dict__)
    source.RevenueGenerated = source.RevenueGenerated+revenue
    source.VolumeHandled = source.VolumeHandled+revenue
    tm = datetime.datetime.now()
    consignments.append([c, tm, tm])
    print("--------BILL---------")
    print("Volume Used: ", cv)
    print("Rate: ", Office.rate)
    print("Total Charges: ", revenue)
    # Update Everything
    allot_truck(c)


def delete_employee():
    eid = input("Enter Employee id:")
    eid = int(eid)
    for emp in employees:
        if emp.EmployeeId == eid:
            employees.remove(emp)
            print("Employee Deleted Successfully")


def employee_menu(cb):
    while True:
        print("--------Branch Employee-----------")
        print("1: Add Consignments")
        print("2: View Sent Consigments")
        print("3: Exit")
        option = input("Enter option: ")
        if option == '1':
            add_consignment_handler(cb)
        elif option == '2':
            view_consignments(cb)
        elif option == '3':
            return
        else:
            print("Enter A valid option: ")


def employee_handler():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    for emp in employees:
        if emp.EmployeeEmailId == email and emp.EmpPassword == password:
            employee_menu(emp.EmployeeBranchId)
            return

    print("Invalid email or password")
    return


def head_manager_menu():
    while True:
        print("----------Head Office----------")
        print("1: Add Truck")
        print("2: Add New Branch")
        print("3: Add Employee")
        print("4: View All Branches")
        print("5: View Trucks")
        print("6: View Employee")
        print("7: Delete Employee")
        print("8: Add Consignment")
        print("9: View Head Office Consginments")
        print("10: View All Consignments")
        print("0: Exit")
        option = input("Enter Option: ")
        if option == '1':
            add_truck_handler()
        elif option == '2':
            add_branch_handler()
        elif option == '3':
            add_employee_handler()
        elif option == '4':
            view_branches()
        elif option == '5':
            view_trucks()
        elif option == '6':
            view_employees()
        elif option == '7':
            delete_employee()
        elif option == '8':
            add_consignment_handler(0)
        elif option == '9':
            view_consignments(0)
        elif option == '10':
            view_all_consignments()
        elif option == '0':
            return
        else:
            print("Please Enter A Valid Option...")


def manager_handler():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    if headManager.EmployeeEmailId == email and headManager.EmpPassword == password:
        head_manager_menu()
    else:
        print("Invalid email or password")
    return


laod_from_file()

while True:
    print("1: Manager")
    print("2: Employee")
    print("3: Exit")

    option = input("Enter Option: ")
    if option == '1':
        manager_handler()
    elif option == '2':
        employee_handler()
    elif option == '3':
        save_to_file()
        break
    else:
        print("Please Enter A Valid Option...")
