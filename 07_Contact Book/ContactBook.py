print("================ Contact Book ================")
print('''
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit ''')

contacts = {
  "rahul": "9876543210",
  "amit": "9988776655",
  "shubham": "9885575226",
  "vaishi": "7452485785"  
}

# ===================== Feature 1 ==================== #
def add_contact():
  name = input("Enter Name :").lower()
  contact = input("Enter contact no. :")
  if len(contact) == 10 and contact.isdigit():
    if name in contacts :
      print("Already Exist")
    else :
      contacts[name] = contact
      print("contact Added")
  else:
    print("Enter valid Number")

# ===================== Feature 2 ==================== #

def view_contact():
  print("======== your contact list ========")
  for index, (name, number) in enumerate (sorted(contacts.items()), start = 1):
    print(f"{index}. {name} : {number}")

# ===================== Feature 3 ==================== #

def search_contact():
  sname = input("Enter name to search :").lower()

  if sname in contacts : 
     print(f"Name : {sname}")
     print(f"Number :{contacts[sname]}")
     return
  else :
    print("contact not in list")

# ===================== Feature 4 ==================== #

def update_contact():
  uname = input("enter name to update :").lower()

  if uname in contacts :
    number = input("Enter new number")
    if len(number) == 10 and number.isdigit():
      contacts[uname] = number
      print("Update succesfully")
    else :
      print("Enter valid number")
  else:
    print("Contact Not Found")

# ===================== Feature 5 ==================== #

def delete_contact():
  dname = input("Enter Name to delete :").lower()

  if dname in contacts :
    contacts.pop(dname)
    print("deleted")
  else :
    print("Contact Not Found")

# ===================== Choices ==================== #

while True :
  user_input = int(input("Enter Your choice as per menu :"))
  if user_input == 1:
    add_contact()

  elif user_input == 2:
    view_contact()

  elif user_input == 3:
    search_contact()

  elif user_input == 4:
    update_contact()

  elif user_input == 5:
    delete_contact()

  elif user_input == 6:
    print("Thank you")
    break

  else:
    print("Invalid Choice")