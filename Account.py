import random

class Account:
    def __init__(self,fullname,cnic,account_name,account_type,password_create) -> None:
        self.fullname =fullname
        self.cnic = cnic
        self.account_name = account_name
        self.account_type =account_type
        self.password_create = password_create
        self.account_number = "ETR-" + "".join([str(random.randint(0, 9)) for _ in range(6)]) + "-" + "".join([str(random.randint(0, 9)) for _ in range(6)])
        self.balance = 0
    def getDocumentDB(self):
        