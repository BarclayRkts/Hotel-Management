import os
import mysql.connector
import random
from datetime import datetime


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
        choice = input("Enter choice")

        if(int(choice) == 1):
           newPatient()
        elif(int(choice) == 2):
            deletePatient()
        elif(int(choice) == 2):
            deletePatient()
        else:
            print("You Entered an Invalid Choice. Try Again")


def manageDoctors():
    pass

def newPatient():
    pass

def deletePatient():
    pass

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