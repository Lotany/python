class Bank:
    #instance attribute
    def __init__(self,name, account_no):
        self.name= name
        self.account_no =account_no

class Employee(Bank):
    def __init__(self, id, name,dept_name,job_allocation,rating=0, mistake= 0):
        super().__init__(id, name)
        self.id =id
        self.name=name
        self.dept_name =dept_name
        self.job_allocation =job_allocation
        self.rating =rating
        self.mistake = mistake

    def view_emp(self):
        print(self.name)

    def add_bonus(self):
        if self.rating >60:
            self.rating +=1000
            print(self.rating)

    def warn_emplyoye(self):
        if self.mistake >10:
            print("You got two warnings left")
class client(Bank):
    def __init__(self,name, account_no, __pin, balance=0):
        super().__init__(id, name, account_no, __pin, balance=0)
        self.name =name
        self.account_no = account_no
        self._pin =__pin
        self._balance =balance

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Cannot make a withdraw")
        elif amount < 0:
            print("cannot withdraw a negative number")
        else:
            self._balance-=amount

    def checkbalance(self):
        query = int(input("Enter pin to viewe balance"))
        if query == self._pin:
            print(self._balance)

data = Bank()