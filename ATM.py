


#Create a record in dictionary   
account = {"username" : "user1" , "pin" : "1234" , "balance" : 5000}


#Checking the user password
def check_pin(pin):
    return pin == account["pin"]

#Creating ATM menu
def show_menu():

    print("Hi ", account["username"])

    print("ATM Menu: ")
    print("1.Check Balance ")
    print("2.Deposit Money ")
    print("3.Withdrawal Money ")
    print("4.Exit")
   
    selected_option = input("pleas enter menu number: ")
    return selected_option

#Creating menu to continue through 
def continuous():
    print("Do you wish to continue? ")
    print("1.Yes")
    print("2.No")

    wish = input ("Answer : ")
    return wish

#ATM
def atm():
    print("Welcome to ATM")
    enter_pin = input("Pleas enter your PIN: ")
    is_pin_valid = check_pin(enter_pin)

    if is_pin_valid == False :
        print("Pin is not correct")

    else :
        selected_option = 0
        wish = "1"
        while selected_option != "4":
            if selected_option != 0:
                wish = continuous()
            if wish == "1" :
                selected_option = show_menu()
            else:
              
                break

            
            if selected_option == "1" :
                print("Your Balance is: ", account["balance"] )
                       
            
            if selected_option == "2" :
                deposit_amount = input("Enter the amount ")
                account["balance"] += int(deposit_amount)
                print("Your new balance is: ", account["balance"] )
                

            if selected_option == "3" :
                deposit_amount = input("Enter the amount ")

                if int(deposit_amount) >= account["balance"]:
                    print("Your amount is not sufficient")

                else:
                    account["balance"] -= int(deposit_amount)
                    print("Your new balance is: ", account["balance"] )

        
            
        print("Pleas take your card.")






atm()