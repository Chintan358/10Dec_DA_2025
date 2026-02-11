from abc import ABC,abstractmethod


class Account(ABC):
    balance = 0
    @abstractmethod # method without implimatation
    def deposite(self,amt):
        pass

    @abstractmethod
    def withdrow(self,amt):
        pass

    def checkbalance(self):
        print(f"current balance is {self.balance}")

class SavingAccount(Account):

    def deposite(self, amt):
        self.balance=self.balance+amt

    def withdrow(self, amt):
        if amt>self.balance:
            print("insufficent amount")
        else:
            self.balance-=amt
    
   
        

s  =SavingAccount()
s.checkbalance()
s.deposite(5000)
s.deposite(1000)
s.checkbalance()
s.withdrow(5000)
s.checkbalance()