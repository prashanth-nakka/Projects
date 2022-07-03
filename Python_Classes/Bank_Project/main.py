'''Simple Bank Project using Python'''


import sys
import time


class Customer:
    '''Customer Class with bank related operations'''
    BANK_NAME = "XYZ Cooperation Bank"
    # operations
    # Constructor

    def __init__(self, name, balance=0.0):
        self.c_name = name
        self.bal = balance

    # Deposit Method
    def deposit(self, amt):
        self.bal += amt
        time.sleep(1)
        print(f"Balance after deposit: {self.bal}")

    # Withdraw Method
    def withdrawl(self, amt):
        if self.bal < amt:
            time.sleep(1)
            print(f"Sorry! Insufficent funds.\n Account Balance: {self.bal}")
            sys.exit()
        else:
            self.bal -= amt
            time.sleep(1)
            print(f"Account Balance after Withdrawl: {self.bal}")

        # Balance Enquiry Method
        def bal_check(self, amt):
            pass

# End of the Class


print(Customer.BANK_NAME)

cust_name = input("Enetr Your Name: ")
if cust_name == "Prashanth":
    print(f"Hi {cust_name}, Good Day!")
else:
    print("Invalid Username!")
    sys.exit()
n = Customer(name=cust_name)
while True:
    option = input(
        "Please select an option from below\n 'D' - Deposit\n 'W' - Withdrawl\n 'E'- Exit\n").lower()

    if option == 'd':
        amt = float(input("Enter Amount: "))
        n.deposit(amt=amt)
    elif option == 'w':
        amt = float(input("Enter Amount: "))
        n.withdrawl(amt=amt)
    elif option == 'e':
        time.sleep(1)
        print("Thanks for Using XYZ Cooperation Bank")
        sys.exit()
    else:
        time.sleep(1)
        print("Invalid option Selected, Kindly Select an option")
