
class Atm(object):
    def __init__(self,pin,numberAtm,cashToWithdraw):
        self.pin = pin
        self.numberAtm =  numberAtm  
        self.cashToWithdraw = cashToWithdraw  
    
    def cashWithdraw(self,cashToWithdraw):
        return(str(self.cashToWithdraw))




pin = input('pin:')
numberAtm = input('atm number:')
amountToTake = input('cash to Withdraw:')


Anvee= Atm(pin,numberAtm,amountToTake)
 


print("cash withdrawed:"+Anvee.cashWithdraw(amountToTake))

