print("================ Expense Tracker ================")

expenses = [
    {
        "title": "pizza",
        "amount": 150,
        "category": "Food"
    },
    {
        "title": "bus ticket",
        "amount": 50,
        "category": "Travel"
    },
    {
        "title": "movie",
        "amount": 200,
        "category": "Entertainment"
    }
]

# =========================== ADD EXPENSES ========================== #
def ADD_EXPENSE():
  title = input("Enter Title :")
  amt = int(input("Enter Amount :"))
  cat = input("Enter Category :")

  new_expense = {
    "title" : title,
    "amount" : amt,
    "category" : cat
  }

  expenses.append(new_expense)
  print("Data Add Successfully")

# ============================== view expenses ================================ #

def VIEW_EXPENSES():
  for expense in expenses :
    print(f"Title : {expense['title']}")
    print(f"Amount : {expense['amount']}")
    print(f"Category : {expense['category']}")
    print("================================")

# ============================= search expenses ========================== #
def SEARCH_EXPENSES():
  user_input = input("Enter title : ").lower()

  for expense in expenses :
    if user_input.lower() == expense["title"]:
      print(f"""title : {expense['title']}
Amount : {expense['amount']}
category : {expense['category']}""")
      return

    else:
      print("Expense Not Found")

# ================= Update expenses ==================== #
def UPDATE_EXPENSES():
    user_input = input("enter title :").lower()

    for expense in expenses:
        if user_input.lower() == expense["title"].lower():
            choice = input("What you want to update amt = a, cat = c, for both = ac :").lower()
            
            if choice == "a":
                amt = int(input("enter amt to update :"))
                expense["amount"] = amt  
                print("Update Successfully")

            elif choice == "c":
                cat = input("Enter category to update :")
                expense["category"] = cat
                print("Update Successfully")

            elif choice == "ac":
                amt = int(input("enter amt to update :"))
                cat = input("Enter category to update :")
                expense["amount"] = amt  
                expense["category"] = cat
                print("Update Successfully")

            else:
                print("Invalid Input")
                
            return  
    
    print("Expense Not Found")

# ======================== Delete Expense ========================== #

def DELETE_EXPENSE():
  user_input = input("Enter Title :").lower()
  for expense in expenses :
    if expense["title"] == user_input :
      expenses.remove(expense)
      print("Expense Delete Successfully")
      return
    else:
      print("expense not found")

# ========================= total expense ==================== #
def TOTAL_EXPENSE():
  total = 0
  for expense in expenses :
    total += expense["amount"] 
  print("Your Total Expense is :", total)



def HIGHEST_EXPENSE():
  high = 0
  for expense in expenses :
    if expense["amount"] > high :
      high = expense["amount"]
      highest_expense = expense

  print(f"Title :{highest_expense['title']}")
  print(f"Amount :{highest_expense['amount']}")
  print(f"category :{highest_expense['category']}")


# ============== MENU ================ #

print(""" 
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Total Expense
7. Highest Expense
8. Exit""")

while True:
  user_input = int(input("Enter input as per Menu :"))
  if user_input == 1:
    ADD_EXPENSE()
  elif user_input == 2:
    VIEW_EXPENSES()
  elif user_input == 3:
    SEARCH_EXPENSES()
  elif user_input == 4:
    UPDATE_EXPENSES()
  elif user_input == 5:
    DELETE_EXPENSE()
  elif user_input == 6:
    TOTAL_EXPENSE()
  elif user_input == 7:
    HIGHEST_EXPENSE()
  elif user_input == 8:
    print("Thank You")
    break
  else :
    print("enter Valid Input")

