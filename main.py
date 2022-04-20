options = {
    'Balance': '200000',
    'Bank': ['access ', 'fidelity', 'ecobank', 'first bank', 'Keystone Bank', 'sterling ', 'wema', 'zenith'],
    'Network': ['airtel', '9mobile', 'mtn', 'glo']

}


def code_info():
    print("""
  The following are the bank code to use to access your account:
  Access  Bank – *901#
  Fidelity Bank – *770#
  EcoBank – *326#
  First Bank – *894#
  Keystone Bank –  *7111#
  Sterling Bank – *822#
  Wema Bank – *945#
  Zenith Bank – *966#
        """)


def intro_message(code):
    print(""" 
    Welcome to self service banking!
        Your defualt pin is 12345
    What will you like to do today?
    Type:
    1 to Check Balance
    2 to Send Money
    3 to Purchase Airtime
        """)


def customer_responses(n):
    password = '12345'
    while n > 0:
        if n == 1:
            print("You have selected check balance")

            user_password = input("Enter pin: ")
            if user_password == password:
                print("Your account balance is ", options['Balance'])
                break
            else:
                print("try again")
        elif n == 2:
            print("You have chosen to send money")
            print("Below are the list of banks, choose one")
            bank_list = options['Bank']
            print("-------------------------------------")
            for i in bank_list:
                print(i)
            print("-------------------------------------")
            user_bank_choice = input("Enter name of bank: ")
            if user_bank_choice in bank_list:
                print("Account number must be 11 digits")
                account_num = input("Enter account number of recipient: ")
                if len(account_num) == 11:
                    amount = int(input("Enter amount to send: "))
                    user_password = input("Enter pin: ")
                    if user_password != password:
                        print("try again")
                    else:
                        user_total = options['Balance']
                        print('Your actual balance is, ', user_total)
                        new_balance = int(user_total) - amount
                        print(
                            'Transaction successful, your new balance is ', new_balance)
                        break

            else:
                print("re enter correct info ")
        elif n == 3:
            print("You have chosen to purchase airtime")
            print("Below are the list of phone networks, choose one,,")
            network_list = options['Network']
            print("-------------------------------------")
            for i in network_list:
                print(i)
            print("-------------------------------------")
            user_network_choice = input("Enter name of network: ")
            if user_network_choice in network_list:
                print("Phone number must be 11 digits")
                phone_num = input("Enter phone number of recipient: ")
                if len(phone_num) == 11:
                    credit = int(input("Enter amount to send: "))
                    user_password = input("Enter pin: ")
                    if user_password != password:
                        print("Try Again")
                    else:
                        user_total = options['Balance']
                        print("Your actual balance is, ", user_total)
                        new_balance = int(user_total) - credit
                        print(
                            "Transaction successful, your new balance is ", new_balance)
                        break
            else:
                print("re enter correct info ")


code_info()
intro_message(input("enter a code: "))
customer_responses(int(input('enter a number: ')))
