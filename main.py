import backend as db
from datetime import date
import random

def menu():

    while True:
        print("************************************************")
        print("*                                              *")
        print("\v*    Welcome to Hospital Management System     *\v")
        print("*                                              *")
        print("************************************************")
        print("------------------------------------------------")
        print("| 1. Administrator Mode                        |")
        print("| 2. User Mode                                 |")
        print("| 3. Exit                                      |\v")
        print("------------------------------------------------")

        choice = input("Enter your mode: ")
        
        if(int(choice) == 1):
            adminMode()
        elif(int(choice) == 2):
            userMode()
        elif(int(choice) == 3):
            exit()
        else:
            print("You Entered an Invalid Moce. Try Again.")
            print("---------------------------------------")
            menu()
            
def managePatients():

    while True:
        print("| 1. Add New Patient                           |")
        print("| 2. Delete Patient                            |")
        print("| 3. Update Details                            |")
        choice = input("Enter choice: ")

        if(int(choice) == 1):
           newPatient()
        elif(int(choice) == 2):
            deletePatient()
        elif(int(choice) == 3):
            updatePatient()
        else:
            print("You Entered an Invalid Choice. Try Again")


def manageDoctors():
    pass

def newPatient():
    print("************************************************")
    print("| A New Patient")
    print("************************************************")
    id = random.randint(0, 1000000)
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    doctor = input("Doctor ID: ")
    birthDate = input("Birth Date (YYYY-MM-DD): ")
    gender = input("Gender (M,F,N): ")
    created = date.today()
    modified = date.today()

    data = (id, firstName, lastName, email, phone, doctor, birthDate, gender, created, modified)
    insertion = db.createPatient(data)

    if insertion != 1:
        print("Patient Successfully Created")
    else:
        print("Something Went Wrong! Try Agian!")
        


def deletePatient():
    print("************************************************")
    print("| Delete Patient")
    print("************************************************")
    id = input("Enter the Patient Id of the Account to Delete: ")
    insertion = db.removePatient(int(id))

    if insertion != 1:   
        print("************************************************")
        print("Patient Successfully Deleted")
        print("************************************************")
    else:
        print("Something Went Wrong! Try Agian!")


def updatePatient():
    pass

    # print("This is the prevID: ", db.getID())
def manageAppointments():
    pass


def adminMode():

    print("************************************************")
    print("| Welcome to Administrator Mode")
    print("************************************************")
    print("Please enter your password: ")
    print("------------------------------------------------")
    password = input("")

    if password == "1234":
        while True:                
            print("| 1. Manage Patients                           |")
            print("| 2. Manage Doctors                            |")
            print("| 3. Manage Appointments                      |")
            print("| 4. Exit                                      |\v")
            print("------------------------------------------------")

            choice = input("Enter your mode: ")
            if(int(choice) == 1):
                managePatients()
            elif(int(choice) == 2):
                manageDoctors()
            elif(int(choice) == 3):
                manageAppointments()
            elif(int(choice) == 4):
                menu()
            else:
                print("You Entered an Invalid Choice. Try Again")

def userMode():
    pass


menu()