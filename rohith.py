import csv

class PassengerRegistration():
    #constructor
    def __init__(self):
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol= 0
        
    def getPassengerInfo(self):
        self.passengerName     = input("Enter Passenger Name          :")
        self.noOfPassenger     = int(input("Enter Number Of Passenger :"))
        print("1: Nagpur")
        print("2: Pune")
        print("3: Mumbai")
        print("4: Delhi")

        # Enter departure Location Name START
        self.dl = int(input("Enter Departure Location"))
        if self.dl == 1:
            self.departureLocation = "Nagpur"
        elif self.dl == 2:
            self.departureLocation = "Pune"
        elif self.dl == 3:
            self.departureLocation = "Mumbai"
        elif self.dl == 4:
            self.departureLocation = "Delhi"
        else:
            print("Please Enter correct choice  :")
        # departure Location Name END
        
        print("1: Gujrat")
        print("2: Raipur")
        print("3: Patna")
        print("4: Bhopal")
        # Enter destination Location Name START
        self.dpl = int(input("Enter Destination Location  :"))
        if self.dpl == 1:
            self.destinationLocation = "Gujrat"
        elif self.dpl == 2:
            self.destinationLocation = "Raipur"
        elif self.dpl == 3:
            self.destinationLocation = "Patna"
        elif self.dpl == 4:
            self.destinationLocation = "Bhopal"
        # Enter destination Location Name END

        self.ddmmyyyy = input("Enter Date of Joiurney Like 07-05-1992   :")  #Date of Journey

        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket  :"))
            if self.seatNo <=30:
                
                if  self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Ticket Allready Booked")
                print("Do You Want To Book One More Seat Enter (Yes/No)") 
                y = input("") 
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("Don't Choose a Seat Number Which is Not Available")    
        # Booking Seat END
        
        print(" 1. AC BUS     = 500 Fare")
        print(" 2. NON AC BUS = 300 Fare")
        self.busType = int(input("Select Bus Type  :"))
        
        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPassenger*500
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPassenger*300
           
        # Booking Seat END
#=============================================
#saving Passenger Data into csv File
#=============================================
class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("D:\\passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                #print(self.data)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("D:\\passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                #w.writerow(["Auto Increment","passenger Name","Number of Passenger","Departure Location","Destination Location","ddmmyyyy","Seat No","Select Bus Type","Bus Fare"])
                w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.selectBusType,self.busFare])
                print("Data Save successfully")
                print()
        

"""pd_obj = PassengerDataCsv()
pd_obj.getPassengerInfo()
pd_obj.saveInfo()"""

#Data Importing section
#from passengerinfo import *

class TicketShow:

    def ticketShow(self):
        bln = [] # list for storing data and retrieving from passengerData.csv file
        with open("D:\\passengerData.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
        #print(bln)  
        print("------------------------------------------------------------------------------")
        print("                               A2R Travels                                         ")
        print("------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :", "Nagpur Address              : Hingna Road Priyadarshini T-Point")
        print("           ", "Phone No\Mob No             : 8000800088,8888880000            ")
        print()
        print("",bln[3],"------------->",bln[4],"            ","        Passenger Id:",bln[0])
        print()
        print(" Passenger Name :", bln[1],"              ","Number of Passenger :",bln[2])
        print("______________________________________________________________________________")
        print()
        print(" Date of Booking :",bln[5],"              ","Seat No :",bln[6],"              ")
        print()
        print(" Bus Type :       ",bln[7],"                                                           ")
        print(" Bus Fare :       ",bln[8],"                                                           ")
        print()
        print("------------------------------------------------------------------------------")
                
import csv
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        print("----------------------------------------------------------------")
        print()
        with open("D:\\adminCredential.csv",'w',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Enter and set username      :")
            self.password = input("Enter and set your password :")
            #saving a data into database
            w.writerow([self.username,self.password])
            print("Registration successfully")
        print()
        print("----------------------------------------------------------------")
            
    def adminLogin(self):
        actList=[] #list for storing data and retrieving from adminCredential.csv file
        
        with open("D:\\adminCredential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actList.append(j)

        #print(actList)
        while(True):
            print("----------------------------------------------------------------")
            print()
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")
            if self.username == str(actList[0]) and self.password == str(actList[1]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password")
            print()
            print("---------------------------------------------------------------")




global ch  # declared global variable

print("---------------------------------------------------")
print("            Welcome To A2R Travels                 ")
print("---------------------------------------------------")
print()

def start(): #called function
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print()
    adminObj = Admin()
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        #admin class object creation
        adminObj.adminRegistration()

    if ch == 2:
        
        adminObj.adminLogin()

        print()
        print("1. Passenger Registration :")
        print("2. Show Ticket            :")
        print()
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            pd_obj = PassengerDataCsv()
            pd_obj.getPassengerInfo()
            pd_obj.saveInfo()
        elif ch ==2:
            obj = TicketShow()
            obj.ticketShow()

#start()#calling function
#=======================================================================
while True:
    print("""1:Get in
2:Exit""")
    dh = int(input("enter your choice :"))
    if dh == 1:
        start()
    elif dh == 2:
        break
    else:
        print("Enter your correct choice")
        




    
