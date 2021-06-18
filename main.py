import os
import mysql.connector
import random
from datetime import datetime


def menu():
    print("\v        Welcome to Hospital Management \v")
    print("1. Administrator Mode")
    print("2. User Mode")
    print("3. Exit \v")

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
        

    # if(int(choice) == 1):
    #     createAccount()
    # elif(int(choice) == 2):
    #     updateInfo()
    # elif(int(choice) == 3):
    #     transaction()
    # elif(int(choice)  == 4 ):
    #     checkAccount()
    # elif(int(choice) == 5):
    #     removeAccount()
    # elif(int(choice) == 6):
    #     viewCustomers()
    # elif(int(choice) == 7):
    #     exit
    # else:
    #     print("You Entered an Invalid Number. Try Again.")
    #     print(">------------------------------------------------")
    #     menu()

def adminMode():
    pass

def userMode():
    pass


menu()