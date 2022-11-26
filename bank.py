class Bank:
    #instance attribute
    def __init__(self,name, account_no):
        self.name= name
        self.account_no =account_no

class Employee(Bank):
    def __init__(self, id, name,dept_name,job_allocation):
        super().__init__(id, name)
        self.id =id
        self.name=name
        self.dept_name =dept_name
        self.job_allocation =job_allocation

class client(Bank):
    def __init__(self,name, account_no, __pin, balance=0):
        super().__init__(id, name, account_no, __pin, balance)
        self.id
