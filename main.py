options = {
    'Balance': '200000',
    'Bank': ['Access Bank', 'Fidelity Bank', 'EcoBank', 'First Bank', 'Keystone Bank', 'Sterling Bank',
             'Wema Bank', 'Zenith Bank'],
    'Network': ['Airtel', '9mobile', 'Mtn', 'Glo']

}


def intro_message(code):
    print(""" 
    Welcome to self service banking!
    What will you like to do today?
    Type:
    1 to Check Balance
    2 to Send Money
    3 to Purchase Airtime
        """)


def customer_responses(n):
    password = '12345'
    if n == 1:
        print("You have selected check balance")

        user_password = input("Enter pin: ")
        if user_password == password:
            print("Your account balance is ", options['Balance'])
        else:
            print("try again")
    elif n == 2:
        print("You have chosen to send money")
        print("Below are the list of banks, choose one")
        bank_list = options['Bank']
        for i in bank_list:
            print(i)
        user_bank_choice = input("Enter name of bank: ")
        if user_bank_choice in bank_list:
            print("Account number is 11 digits")
            account_num = input("Enter account number of recipient: ")
            if len(account_num) == 11:
                amount = int(input("Enter amount to send: "))
                user_password = input("Enter pin: ")
                if user_password == password:
                    user_total = options['Balance']
                    new_balance = int(user_total) - amount
                    print('Transaction successful, your new balance is ', new_balance)
    elif n == 3:
        print("You have chosen to purchase airtime")
        print("Below are the list of phone networks, choose one,,")
        network_list = options['Network']
        for i in network_list:
            print(i)
        user_network_choice = input("Enter name of network: ")
        if user_network_choice in network_list:
            print("Phone number must be  11 digits")
            phone_num = input("Enter phone number of recipient: ")
            if len(phone_num) == 11:
                credit = int(input("Enter amount to send: "))
                user_password = input("Enter pin: ")
                if user_password != password:
                    pass
                else:
                    user_total = options['Balance']
                print('Your actual balance is, ', user_total)
                new_balance = int(user_total) - credit
                print('Transaction successful, your new balance is ', new_balance)
    else:
        print("not in the type")


intro_message(input("enter a code: "))
customer_responses(int(input('enter a number: ')))
