print("==================== ATM ====================")

BANK_USER = {
  123456 : {
     "password": "ABC",
      "name": "Rahul",
      "balance": 50000
  },
  678912 : {
    "password": "XYZ",
    "name": "Amit",
    "balance": 25000
  }
}

history = []

attempt = 0
while(attempt < 3):
  user = int(input("Enter your Acc No. :"))

  if user in BANK_USER :
    password = input("Enter Password. :")

    if password == (BANK_USER[user]["password"]):
      print ("welcome to XYZ Bank")
      print("HELLO ", BANK_USER[user]["name"])

      print('''
  ============ ATM Menu ===========
  1. Check Balance
  2. Deposite Money
  3. Withdraw Money 
  4. Transaction History
  5. Exit 
  =================================
  ''')

    while True :
        try:
          take_input = int(input("Enter input to further process as per upper instruction :"))
        except ValueError:
          print("Please enter a valid number.")
          continue

        if take_input == 1 :
          print("Your current balance is ", BANK_USER[user]["balance"])
          
        elif take_input == 2 :
          deposite = int(input("Enter Amount to deopsite :"))
          if deposite <= 0:
            print("Invalid Amount")
          else :
            BANK_USER[user]["balance"] += deposite
            print(f" ₹{deposite} Deposite Successfully")
            history.append(f"deposited ₹{deposite}")
            print("Updated Balance:", BANK_USER[user]["balance"])

        elif take_input == 3 :
          withdraw = int(input("Enter Amount to withdraw :"))
          if (withdraw <= 0):
            print("Invalid Amount")
          elif (withdraw > BANK_USER[user]["balance"]):
            print("Insufficient Balance")
          else :
            BANK_USER[user]["balance"] -= withdraw
            print(f"₹{withdraw} withdraw Successfully")
            history.append(f"withdraw ₹{withdraw}")
            print("Updated Balance:", BANK_USER[user]["balance"])

        elif take_input == 4 :
            for index, h in enumerate(history, start = 1):
              print(f"{index}.{h}")

        elif take_input == 5 :
          print("thank You for using atm")
          break
        else :
          print("invalid input")
          
          
    break
      
      
  else : 
      print ("incorrect password")
      attempt += 1
else : 
  print("Details Not Found")
  attempt += 1 

if attempt == 3 :
  print("Too many attempt: Account Locked")

