class bank:
    customer_name = ""
    account_number = ""
    account_type = ""
    account_balance = 0

    def __init__(self, a_name, a_no, a_type, a_balance):
        self.customer_name = a_name
        self.account_number = a_no
        self.account_type = a_type
        self.account_balance = a_balance

    def deposite(self, deposit):
        print("MAain Balance is  : ", self.account_balance)
        print("Deposite is  : ", deposit)
        self.account_balance += deposit
        print("Current balance is  : ", self.account_balance)

    def withdraw(self):
        print("Current balance is  : ", self.account_balance)
        self.amount = int(input("Ener Amount to withdraw : "))
        if self.amount > self.account_balance:
            print("You don't have enough balance to withdraw !!")
            print("Current balance is  : ", self.account_balance)
        else:
            print(self.amount, " is withrawed .")
            self.account_balance -= self.amount
            print("Current balance is  : ", self.account_balance)

    def acc_info(self):
        print(
            "\n\n*********************************************************************************************************************\n\n")
        print("Account holder name  :  ", self.customer_name)
        print("Account number         :  ", self.account_number)
        print("Account type              :  ", self.account_type)
        print("Account Balance is      :  ", self.account_balance)
        print(
            "\n\n*********************************************************************************************************************\n\n")


def main():
    name = input("Enter Account holder name : ")
    no = input("Enter Account number        : ")
    atype = input("Enter Account type             : ")
    bal = int(input("Enter Account initial balance : "))
    holder = bank(name, no, atype, bal)

    while (True):
        print("\n\n.........................................................\n\n")
        opt = int(input("1)Deposite \n2)Withdraw \n3)Account info \n0)Exit\nChoose your option :: "))
        print("\n\n.........................................................\n\n")
        if opt == 1:
            amount = int(input("Deposite amount : "))
            holder.deposite(amount)
        elif opt == 2:
            holder.withdraw()
        elif opt == 3:
            holder.acc_info()
        elif opt == 0:
            break
        else:
            print("Invalid Option !")


if __name__ == "__main__":
    while (True):
        main()
