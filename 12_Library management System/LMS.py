print("============= Library Management System ============== #")

books = [
    {
        "id": "B101",
        "title": "Python Basics",
        "author": "Guido",
        "available": True
    },
    {
        "id": "B102",
        "title": "Data Structures",
        "author": "Mark",
        "available": False
    }
]


def ADD_BOOK():
    id = input("Enter Book Id :")
    for book in books :
       if id.title() == book["id"]:
          print("Book id Already Exist")
          return
    else :
      title = input("Enter Book Title :")
      author = input("Enter Book Author :")
      available = input("Is book Available : (True/False) :").title()
      if available == "True"  :
        available = True
      elif available == "False"  :
        available = False
      else :
        print("Enter valid Input")
      new_book = {
        "id" : id,
        "title" : title,
        "author" : author,
        "available" : available
      }
      books.append(new_book)
      print("Data Add Successfully")
 

def VIEW_BOOK():
   for book in books :
      print(f"id : {book['id']}")
      print(f"title : {book['title']}")
      print(f"author : {book['author']}")
      print(f"available : {book['available']}")
      print("**************************")

def SEARCH_BOOK():
   id = input("Enter Book Id :").upper()
   for book in books :
      if id.title() == book["id"]:
         print(f"id : {book['id']}")
         print(f"title : {book['title']}")
         print(f"author : {book['author']}")
         print(f"available : {book['available']}")
         return
      
   print("Book Not Found")


def BOOK_BORROW():
   id = input("Enter Book Id :") 
   for book in books :
      if id.title() == book["id"] :
         if book["available"] == True :
            print("Book Borrowed Successfully")
            book["available"] = False
            return
         elif book["available"] == False :
            print("Book is already borrowed.")
            return
   else :
    print("Enter Valid Id")
    return

def RETURN_BOOK():
   id = input("Enter Book id :").upper()
   for book in books :
      if id.title() == book["id"] :
         if book["available"] == True :
            print("No book Issued")
            return
         elif book["available"] == False :
            user = input("want to retun book :(yes/no)").lower()
            if user == "yes":
              book["available"] = True
              print("Thank You....!")
              return
   else :
      print("Book Not Found")
      return
            

def DELETE_BOOK():
   id = input("Enter Book Id :")
   for book in books :
      if id.title() == book["id"]:
         books.remove(book)
         print("Data Deleted...!")
         return
   else :
      print("Enter valid id")
      return

def TOTAL_BOOKS():
   total_book = 0
   avail = 0
   borrow = 0

   for book in books :
      total_book += 1
      if book["available"] == True :
         avail += 1
      else :
         borrow += 1

   print(f"Total Book : {total_book}")
   print(f"Available : {avail}")
   print(f"Borrowed : {borrow}")


print(""" 
1. Add Book
2. View Books
3. Search Book
4. Borrow Book
5. Return Book
6. Delete Book
7. Total Books
8. Exit """)

while True:
  user_input = int(input("Enter input as per Menu :"))
  if user_input == 1:
    ADD_BOOK()
  elif user_input == 2:
    VIEW_BOOK()
  elif user_input == 3:
    SEARCH_BOOK()
  elif user_input == 4:
    BOOK_BORROW()
  elif user_input == 5:
    RETURN_BOOK()
  elif user_input == 6:
    DELETE_BOOK()
  elif user_input == 7:
    TOTAL_BOOKS()
  elif user_input == 8:
    print("Thank You")
    break
  else :
    print("enter Valid Input")
