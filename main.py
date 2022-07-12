import time
from getpass import getpass
# global loggg = 0


class hotelfarecal:
    log_count = 0
    first_count = 0
    room_no_count = 0

    def __init__(
        self,
        rt="",
        s=0,
        p=0,
        r=0,
        t=0,
        a=1800,
        days="",
        date="",
        cindate="",
        person="",
        room="",
        rno=0,
    ):

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.days = days
        self.date = date
        self.cindate = cindate
        self.person = person
        self.room = room
        self.rno = hotelfarecal.room_no_count + 1
        hotelfarecal.room_no_count = hotelfarecal.room_no_count + 1

    def reg(self):
        print("\n\nRegister!\n\n")
        global user
        global psw
        global fn
        global ln
        user = str(input("New Email: "))
        fn = str(input("First Name: "))
        ln = str(input("Last Name: "))
        dob = str(input("Date of Birth: "))
        psw = getpass("New Password: ")
        print("\n\nPassword and Username has been set successfully! continue.\n\n")

    def login(self):
        print("\n\nLogin with Username and Password!\n\n")
        login_username = str(input("Email: "))
        login_password = getpass("Password: ")
        if(login_username != user or login_password != psw):
            # print("\x1B[2J")
            print("Username or password is incorrect please try again!")
            login()
        else:
            print("\n\nSuccess!\n")

    def inputdata(self):
        f = open("database.txt", "w")
        self.days = input("\n\nNumber of days: ")
        f.write("Number of days: " + self.days)
        self.date = input("From Date: ")
        f.write("From date: " + self.date)
        self.cindate = input("To Date: ")
        f.write("To date: " + self.cindate)
        self.person = input("Number of Persons: ")
        f.write("Number of persons" + self.person)
        self.room = input("Number of Rooms: ")
        f.write("Number of rooms" + self.room)
        f.close()

    def modifydata(self):
        f = open("database.txt", "w")
        self.days = input("Number of days: ")
        f.write("Number of days: " + self.days)
        self.date = input("From Date:")
        f.write("From date: " + self.date)
        self.cindate = input("To Date:")
        f.write("To date: " + self.cindate)
        self.person = input("Number of Persons:")
        f.write("Number of persons" + self.person)
        self.room = input("Number of Rooms:")
        f.write("Number of rooms" + self.room)
        f.close()

    def deletedata(self):
        f = open("database.txt", "w")
        self.days = ""
        self.date = ""
        self.cindate = ""
        self.person = ""
        self.room = ""
        f.write("Number of days: " + self.days)
        f.write("From date: " + self.date)
        f.write("To date: " + self.cindate)
        f.write("Number of persons" + self.person)
        f.write("Number of rooms" + self.room)
        f.close()

    def display(self):
        print("\n\nFirst name: ", fn)
        print("Last name: ", ln)
        print("Number of days: ", self.days)
        print("From date: ", self.date)
        print("To date: ", self.cindate)
        print("Number of persons: ", self.person)
        print("Number of rooms: ", self.room)


def main():

    rooms = []
    a = None  # object of class
    count = 0
    log = 0
    while 1:
        print("\n1.Register/signup")

        print("2.Login")

        print("3.EXIT")

        b = int(input("\n\nEnter your choice: "))
        if b == 1:
            a = hotelfarecal()
            # rooms.append({"room_no": a.rno})
            a.reg()
            count += 1
        if b == 2:
            # global choise
            # try:
            if count == 0:
                print("\n\nNo Record Found, register first.\n\n")
            else:
                a.login()
                while 1:
                    print("\n\n1.View Reservation")

                    print("2.Make Reservation")

                    print("3.Modify Reservation")

                    print("4.Cancel Reservation")

                    print("5.Logout\n")

                    choise = int(input("\n\nEnter your choice: "))
                    if choise == 1:
                        if log == 0:
                            print("No Record Found, make a reservation first.")
                        else:
                            a.display()
                    elif choise == 2:
                        log += 1
                        a.inputdata()
                    elif choise == 3:
                        if log == 0:
                            print("No Record Found, make a reservation first.")
                        else:
                            a.modifydata()
                    elif choise == 4:
                        if log == 0:
                            print("No Record Found, make a reservation first.")
                        else:
                            a.deletedata()
                            print("\nReservation Cancelled")
                    else:
                        break
        if b == 3:
            quit()


main()
