class Atm:

    def __init__(self):
        
        self.pin = ''
        self.balance = 0

        self.menu()

    def menu(self):
        user_input= input("""
                        Hello! How can I help you??
                     
                        1. Press 1 to set pin
                        2. Press 2 to deposit
                        3. Press 3 to withdraw
                        4. Press 4 to check balance
                        5. Press 5 to exit
                     
                    """)
        
        if user_input == '1':
            self.set_pin()

        if user_input== '2':
            self.deposit()

        if user_input== '3':
            self.withdraw()

        if user_input=='4':
            self.check_balance()

        if user_input=='5':
            print('Bye!!See you next time!')


    def set_pin(self):
        self.pin = input('Set ypur pin:')
        print('PIN set')

    def deposit(self):
        temp = input('Enter your pin:')

        if temp == self.pin:
            amount = int(input('Enter the amount:'))

            self.balance = self.balance + amount

            print('Amount deposited')

        else:
            print('Invalid pin')

    def withdraw(self):
        temp = input('Enter your pin:')

        if temp == self.pin:
            amount = int(input('Enter the amount:'))

            if amount < self.balance:
                self.balance = self.balance - amount

                print('Amount withdrawn')

            else:
                print('Insufficient funds')
        else:
            print('Invalid pin')

    def check_balance(self):
        temp = input('Enter your pin:')

        if temp == self.pin:
            print(f'Your balance is {self.balance}')
        else:
            print('Invalid pin')

        

