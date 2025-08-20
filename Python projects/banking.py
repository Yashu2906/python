class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("You account is debited by ",amount,"Rupees.")
        print("Total balance is ",self.balance,".")

    def credit(self,amount):
        self.balance += amount
        print("You account is credit by ",amount,"Rupees.")
        print("Total balance is ",self.balance,".")


a1 = Account(10000,7901000)
a1.debit(600)
a1.credit(10000)