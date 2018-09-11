class Bank:
    def __init__(self,name,account_no,balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposite(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        self.balance -= ammount

    def __str__(self):
        return 'Name:{} Balance:{}'.format(self.name, self.balance)

    def __repr__(self):
        return 'Account Number:{}'.format(self.account_no)

if __name__ == '__main__':
    b1 = Bank('santosh', 9988, 200)
    print(b1)
    print(b1.balance)
    b1.deposite(900)
    print(b1.balance)
    b1.withdraw(100)
    print(b1)
