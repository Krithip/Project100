class atm:
    def __init__(self, pinNumber, cardNumber):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
    def checkBalance(self):
        print("Your balance is 20")
    def withdrawel(self, amount):
        newAmount = 20 - amount
        print(newAmount)
def main():
    cardNumber = input("Enter your card number")
    pinNumber = input("Enter your pin number")
    a1 = atm(pinNumber, cardNumber)
    print("Choose your activity, 1. Balance Enquiry, 2. Withdrawel")
    activity = int(input("Enter the activity number"))
    if(activity == 1):
        a1.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter the amount you would like to withdraw"))
        a1.withdrawel(amount)
    else:
        print("Enter a valid number")
if __name__ == "__main__":
    main()