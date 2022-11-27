class Bank:
    #instance attribute
    def __init__(self,name, account_no,m_pass=1111):
        self.name =name
        self.account_no = account_no
        self.m_pass = m_pass
class Client(Bank):
    #inatance attribute
    def __init__(self, name, account_no, __pin=0000, balance = 0,login=1,logout =0):
        super().__init__(name, account_no)
        self.name =name
        self.account_no =account_no
        self.__pin =__pin
        self.balance = balance
        self.login =login
        self.logout =logout

    #instace method
    def deposit(self, amount):
        if amount < 0:
            print("Cannot depoesit a negative value....")
        else:
            self.balance +=amount

    def withdraw(self, amount):
        if self.balance <amount:
            print('Not sufficient money to wthdraw please try again.....')
        else:
            self.balance +=amount
    
    def check_balance(self):
        query = int(input("Enter pin to  check balance: "))
        if query == self.__pin:
            print(f"Your balance is: {self.balance}")
        else:
            print(f"Wrong password try again")

    def log_in(self):
        print('Enter username')
        var = input()
        print('Enter pass: ')
        var1 = int(input())

        if var != self.name and var1 !=self.m_pass:
            print("Wrong credentials: ")
            quit()
        else:
            print(f"{self.name} your balance is {self.balance}")
            print("Withdraw")
            var3 =int(input())
            self.balance -= var3
        print(f"Your balance is now {self.balance} ")

mylist =[Client("Lotan",1234)]

bank1 = Client("lotan",1234)

bank1.deposit(20000)

bank1.log_in()


