print("========== Inventory Management System ==========")

products = {
    "P101": {
        "name": "Laptop",
        "price": 50000,
        "stock": 10
    },

    "P102": {
        "name": "Laptop",
        "price": 50000,
        "stock": 10
        },

    "P103": {
        "name": "Laptop",
        "price": 50000,
        "stock": 10
    }
}

# ============================= ADD PRODUCTS ======================== #
def ADD_PRODUCT():
  pcode = input("Enter Product Code :")
  if pcode in products :
    print("product already exist")

  else:
    pname = input("enter product name")
    pprice = int(input("enter product price"))
    pstock = int(input("enter product stock"))

    products[pcode] = {
      "name" : pname,
      "price" : pprice,
      "stock" : pstock
    }
    print("Add product succesfully ")

# ============================= VIEW PRODUCTS ======================== #

def VIEW_PRODUCTS():
  for pcode in products :
    print(pcode)
    print("Product Name :",products[pcode]["name"])
    print("Product Price :",products[pcode]["price"])
    print("Product Stock :",products[pcode]["stock"])
    print("")

# ============================= SEARCH PRODUCTS ======================== #

def SEARCH_PRODUCT():
  pcode = input("Enter Product Code :")
  if pcode in products :
    product = products[pcode]
    print("Product Name :",product["name"])
    print("Product Price :",product["price"])
    print("Product Stock :",product["stock"])
  else : 
    print("product not found")

# ============================= UPDATE PRODUCTS ======================== #

def UPDATE_PRODUCT():
  pcode = input("Enter code to update :").upper()
  if pcode in products :
    user = input("Enter what you want to update stock=(s)/price=(p) :").upper()
    if user == "S" :
      Add = input("Want to increase or decrease stock 'I/D' :").upper()
      if Add == "I" :
        stock = int(input("Enter Updated stock :"))
        data = products[pcode]
        data["stock"] += stock
        print("Product Name :", data["name"])
        print("Product Qty :", data["stock"])
      elif Add == "D":
        stock = int(input("Enter Updated stock :"))
        if stock < products[pcode]["stock"]:
          data = products[pcode]
          data["stock"] -= stock
          print("Product Name :", data["name"])
          print("Product Qty :", data["stock"])
        else:
          print("Enter Valid Stock")
      else:
        print("""Print valid input only :
         if you want to increase stock enter = I 
         if you want to decrease stock enter = D """)

    elif user == "P":
      Add = input("Want to increase or decrease stock 'I/D' :").upper()
      if Add == "I" :
        price = int(input("Enter Updated price :"))
        data = products[pcode]
        data["price"] += price
        print("Product Name :", data["name"])
        print("Product Price :", data["price"])
      elif Add == "D":
        price = int(input("Enter Updated price :"))  
        if price < products[pcode]["price"]:
          data = products[pcode]
          data["price"] -= price
          print("Product Name :", data["name"])
          print("Product price :", data["price"])
        else:
          print("Enter Valid price")

    else:
      print("""Print valid input only :
      if you want to increase stock enter = I 
      if you want to decrease stock enter = D """)

  else :
    print("this code of product is not available")

# ============================= DELETE PRODUCTS ======================== #
def DELETE_PRODUCT():
  pcode = input("Enter product code to delete :").upper()
  if pcode in products :
    products.pop(pcode)
    print("delete data successfully")
  else:
    print("product not found")


def TOTAL_VALUE():
  total = 0
  for data in products.values():
    total += data["price"] * data["stock"]

  print("Total value is :",total)
# ============================= OPERATIONS FOR PRODUCTS ======================== #

print('''
1. Add product
2. View product
3. Search product
4. Update product
5. Delete product
6. Total Value of Inventory
7. Exit''')

# ===================== INPUT FOR OPERATION ================ #
while True:
  user_input = int(input("Enter input as per Menu :"))
  if user_input == 1:
    ADD_PRODUCT()
  elif user_input == 2:
    VIEW_PRODUCTS()
  elif user_input == 3:
    SEARCH_PRODUCT()
  elif user_input == 4:
    UPDATE_PRODUCT()
  elif user_input == 5:
    DELETE_PRODUCT()
  elif user_input == 6:
    TOTAL_VALUE()
  elif user_input == 7:
    print("Thank You")
    break
  else :
    print("enter Valid Input")