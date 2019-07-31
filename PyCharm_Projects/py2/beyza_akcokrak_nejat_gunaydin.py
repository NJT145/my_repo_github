#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def current_datetime():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 'Year-Mounth-Day Hour:Minute.Second'


class Transaction(object):
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
        self.timestamp = current_datetime()

    def get_info(self):
        return (self.timestamp, self.from_user, self.to_user, self.amount)

    def transaction_type(self):
        if self.from_user != self.to_user:
            return "transfer"
        if self.amount < 0:
            return "withdraw"
        return "deposit"


class User(object):
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.balance = 0  # always >=0
        self.transaction_counter = 0
        self.deposits = {}
        self.withdrawals = {}
        self.transfers = {}

    def get_username(self):
        return self.name

    def get_password(self):
        return self.password

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount

    def add_transaction(self, transaction):
        self.transaction_counter += 1
        index = self.transaction_counter
        info = transaction.get_info()
        if transaction.transaction_type() == "deposit":
            self.deposits[index] = "Deposited " + str(info[3]) + " " + str(info[0])
        elif transaction.transaction_type() == "withdraw":
            self.withdrawals[index] = "Withdrawed " + str(-info[3]) + " " + str(info[0])
        elif transaction.transaction_type() == "transfer":
            if info[1] == self.get_username():
                self.transfers[index] = "Transfered " + str(info[3]) + " to " + str(info[2]) + " " + str(info[0])
            else:
                self.transfers[index] = "Transfered " + str(info[3]) + " to me from " + info[1] + " " + str(info[0])

    def get_transactions(self):
        transactions = []
        for index in range(1, self.transaction_counter + 1):
            if index in self.deposits.keys():
                transactions.append(self.deposits[index])
            elif index in self.withdrawals.keys():
                transactions.append(self.withdrawals[index])
            elif index in self.transfers.keys():
                transactions.append(self.transfers[index])
            else:
                raise IndexError("Transaction Error!!!")
        return transactions

    def get_deposits(self):
        return self.deposits

    def get_withdrawals(self):
        return self.withdrawals

    def get_transfers(self):
        return self.transfers

    def do_deposit_withdraw(self, amount):
        self.add_balance(amount)  # do deposit (positive amount) or withdraw (negative amount)

    def user_info(self):
        return [self.get_username(), self.get_password(), self.get_balance(), self.get_transactions()]


class DataStorageInterface(object):
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, username, password):
        self.users[username] = User(username, password)

    def get_user(self, username):
        return self.users[username]

    def check_transaction(self, from_user, to_user, amount):
        if from_user != to_user:  # transfer transaction
            if amount > self.get_user(from_user).get_balance():  # transfer transaction error
                return False
            return True  # transfer is possible
        else:  # deposit or withdraw transaction
            if amount < 0:  # withdraw transaction
                if -amount > self.get_user(from_user).get_balance():  # withdraw transaction error
                    return False
                return True  # withdraw is possible
            return True  # no error for deposit transactions


class DataStorage(DataStorageInterface):
    def __init__(self):
        super(DataStorage, self).__init__()
        self.current_user = None

    def login(self, username, password):
        try:
            self.current_user = self.get_user(username)
        except:
            self.current_user = None
        else:
            if self.current_user.get_password() == password:
                return True
        return False

    def logout(self):
        self.current_user = None

    def add_deposit(self, amount):
        if amount < 0:  # amount error
            return "amountError"
        username = self.current_user.get_username()
        is_possible = self.check_transaction(username, username, amount)
        if is_possible:
            self.current_user.do_deposit_withdraw(amount)
            self.current_user.add_transaction(Transaction(username, username, amount))
            return "done"
        return "notPossible"

    def add_withdraw(self, amount):
        if amount < 0:  # amount error
            return "amountError"
        username = self.current_user.get_username()
        is_possible = self.check_transaction(username, username, -amount)
        if is_possible:
            self.current_user.do_deposit_withdraw(-amount)
            self.current_user.add_transaction(Transaction(username, username, -amount))
            return "done"
        return "notPossible"

    def add_transfer(self, to_user, amount):
        try:
            other_user = self.get_user(to_user)
        except:
            raise ValueError("User does not exist!!")
        else:
            if amount < 0:  # amount error
                return "amountError"
            from_user = self.current_user.get_username()
            is_possible = self.check_transaction(from_user, to_user, amount)
            if is_possible:
                transaction = Transaction(from_user, to_user, amount)
                self.current_user.do_deposit_withdraw(-amount)
                other_user.do_deposit_withdraw(amount)
                self.current_user.add_transaction(transaction)
                other_user.add_transaction(transaction)
                return "done"
            return "notPossible"

    def get_current_user(self):
        return self.current_user


class BankApp(object):
    def __init__(self):
        self.datastore = DataStorage()
        self.datastore.add_user("Ahmed", "1234")
        self.datastore.add_user("Erva", "4321")
        self.datastore.add_user("Ayse", "4422")
        self.service_error = "Please enter a number that is a valid input."
        self.login_error = "Wrong User Name or Password. Please Try Again!"
        self.input_error = "Please enter a valid input."

    def run(self):
        return self.welcome_page()

    def welcome_page(self):
        print("\n" + "|" + ("-" * 35) + "|")
        print((" " * 5) + "Welcome To Sehir Bank v0.3")
        print("\n" + "|" + ("-" * 35) + "|")
        print((" " * 5) + "ISTANBUL " + current_datetime())
        print("\n" + "|" + ("-" * 35) + "|")
        print("< Choose what do you want to do. >\n< 1. Login >\n< 2. Exit >")
        service_welcome = raw_input(">>> ")
        if service_welcome == "1":  # Login
            current_user_name = self.login_user()
            print(" Login Success!\n Transferring...")
            print("\nHello, " + current_user_name)
            return self.login_user_page()
        elif service_welcome == "2":  # Exit
            return
        else:  # invalid input/service_number
            print(self.service_error)
            return self.welcome_page()

    def login_user(self):
        username = raw_input("User Name:")
        password = raw_input("Password:")
        login_check = self.datastore.login(username, password)
        if login_check:
            return username
        print(self.login_error)
        return self.login_user()

    def login_user_page(self):
        print("<" + ("=" * 27) + " Bank Services Available " + ("=" * 27) + ">")
        print("\nChoose Service")
        print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Logout")
        print("<" + ("=" * 79) + ">")
        selected_service = raw_input(">>>")
        if selected_service == "1":  # Withdraw Money
            self.withdraw()
        elif selected_service == "2":  # Deposit Money
            self.deposit()
        elif selected_service == "3":  # Transfer Money
            self.transfer()
        elif selected_service == "4":  # Show Account Information
            self.account_info()
        elif selected_service == "5":  # Logout - return to welcome_page()
            self.datastore.logout()
            return self.welcome_page()
        else:  # invalid input/service_number
            print(self.service_error)
        return self.login_user_page()

    def deposit(self):
        try:
            money_input = int(raw_input("\nHow much do you wish to deposit ? "))
        except:
            print(self.service_error)
        else:
            check_deposit = self.datastore.add_deposit(money_input)
            if check_deposit == "notPossible":
                print("Transaction is not possible...\nGoing back to main menu...")
            elif check_deposit == "amountError":
                print("Please enter a positive number at next time.\nGoing back to main menu...")
            elif check_deposit == "done":
                print(str(money_input) + " TL has been deposited to your account.")
                print("You have deposited " + str(money_input))

    def withdraw(self):
        try:
            money_input = int(raw_input("\nHow much do you wish to withdraw ? "))
        except:
            print(self.service_error)
        else:
            check_withdraw = self.datastore.add_withdraw(money_input)
            if check_withdraw == "notPossible":
                print("You don't have " + str(money_input) + " TL in your account.\nGoing back to main menu...")
            elif check_withdraw == "amountError":
                print("Please enter a positive number at next time.\nGoing back to main menu...")
            elif check_withdraw == "done":
                print(str(money_input) + " TL has been withdrawn from your account.")

    def transfer(self, to_user=None, repeating=False):
        if repeating:
            service_transfer = raw_input(" 1. Transfer again.\n 2. Go back to main menu.\n>>>")
            if service_transfer == "1":
                return self.transfer(to_user=to_user)
            elif service_transfer == "2":
                return
            else:
                print(self.service_error)
                return self.transfer(to_user=to_user, repeating=repeating)
        if to_user is None:
            to_user = raw_input("\nFor who do you wish to transfer to ? ")
        try:
            self.datastore.get_user(to_user)
        except:
            print("User doesn't exist.\nGoing back to main menu...")
            return
        if self.datastore.get_current_user().get_username() == to_user:
            print("You can not make transfer to yourself.\nGoing back to main menu...")
            return
        try:
            money_input = int(raw_input("How much would you like to transfer ? "))
        except:
            print(self.service_error)
            return self.transfer(to_user=to_user, repeating=True)
        else:
            check_transfer = self.datastore.add_transfer(to_user, money_input)
            if check_transfer == "notPossible":
                print("You don't have " + str(money_input) + " TL in your account.")
                return self.transfer(to_user=to_user, repeating=True)
            elif check_transfer == "amountError":
                print("Please enter a positive number at next time.\nGoing back to main menu...")
            elif check_transfer == "done":
                print("Transfering " + str(money_input) + " TL to " + to_user + " Succeeded.")

    def account_info(self):
        user_info = self.datastore.get_current_user().user_info()
        current_time = current_datetime()
        print("|" + ("_" * 15) + " User Data " + ("_" * 16) + "|")
        print("Date:  " + current_time.split(" ")[0] + "\nTime:  " + current_time.split(" ")[1])
        print("    User:  " + str(user_info[0]))
        print("    Password:  " + str(user_info[1]))
        print("    Balance:  " + str(user_info[2]))
        print("|" + ("_" * 14) + " Transactions " + ("_" * 14) + "|")
        for transaction in user_info[3]:
            print("    " + transaction)


bank_app = BankApp()
bank_app.run()
