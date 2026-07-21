# =========================== OOPS In Python ============================ #

# ************ Class & Object ************** #

# class student :
#   Name = "Shubham"
#   MiddleName = "Gajanan"
#   LastName = "Bahe"

# S1 = student()
# print(S1.MiddleName)
# print(S1.Name)

# print(type(S1.Name))


# **************************** Init Function // Constructor in python *************************** #

# class Student :
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks
#     print("adding data into database")

#   def welcome(self):
#     print("welcome lodu,", self.name)

#   def get_marks(self):
#     print ("ye hai teri layki bc :", self.marks)

# s1 = Student("shubham", 85)
# print(s1.name, s1.marks)

# s1.welcome()
# s1.get_marks()

# # s2 = Student("vaishnavi", 75)
# # print(s2.name, s2.marks)




# **************************** Practice Question *************************** #

# create student class that take name & marks of 3 subjects as arguement in constructor 
# then create a method to print the average


# class student : 

  
#   def __init__(self, name, subject1, subject2, subject3, marks1, marks2, marks3):
#     self.name = name
#     self.subject1 = subject1
#     self.subject2 = subject2
#     self.subject3 = subject3
#     self.marks1 = marks1
#     self.marks2 = marks2
#     self.marks3 = marks3
#     print("here is an result of question")

#   def avg(self):
#     print (((self.marks1) + (self.marks2) + (self.marks3)) / 3)

# s1 = student("shubham",  "math", "sci", "eng", 85, 75, 97)
# print(
#       s1.name, 
#       s1.subject1, s1.marks1, 
#       s1.subject2, s1.marks2, 
#       s1.subject3, s1.marks3 
# )

# s1.avg()



# ==================== Another way to solve =============================== #

# class Student :

#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def avg_marks(self):
#     sum = 0
#     for i in self.marks :
#       sum += i
#     print("hi", self.name, "your avg of marks is :", sum/len(self.marks)) 


# s1 = Student("shubham", [85, 75, 97, 85])
# s1.avg_marks()


# ================== Account management system ================== #

# class Account: 

#   def __init__(self, Account, Balance):
#     self.Account = Account
#     self.Balance = Balance

#   def debit (self, amount):
#     self.Balance -= amount
#     print(amount, "debited from your account")
#     print("total balance id ", self.Balance)


#   def credit (self, amount):
#     self.Balance += amount
#     print(amount, "credited in your account")
#     print("total balance is ", self.Balance)

#   def transfer (self, acc, amount):
#     self.acc = acc
#     if acc == Acc1 :
#       print(self.balance - amount)

#   def balance (self, amount):
#     return self.Balance


# Acc1 = Account(12345, 10000)
# Acc2 = Account(12346, 5000)

# Acc1.transfer(Acc1, 2000)


# def BigNum(n1, n2, n3):
#   if n1 > n2 and n1 > n3 :
#     print(n1, "is greater")
#   elif n2 > n1 and n2 > n3 :
#     print(n2, "is greater")
#   elif n3 > n2 and n3 > n1 :
#     print(n3, "is greater")
#   elif n1 == n2 == n3 :
#     print("equal")
#   else :
#     return "error"

# BigNum(56, 98, 46)


# def count_vowelt (text):
#   count = 0
#   for ch in text :
#       if ch == "a":
#         count += 1
#       elif ch == "e":
#          count += 1
#       elif ch == "i":
#          count += 1
#       elif ch == "o":
#          count += 1
#       elif ch == "u":
#          count += 1
#   else: 
#     return count
# count_vowel("shubham")


# def palindrome(text):

#   if text == (text[::-1]):
#     print("true")
#   else :
#     print("fa")

# palindrome("shubham")


# def palindrome(text):

#   reverse_text = ""
#   for ch in text:
#     reverse_text = ch + reverse_text
#   if text == reverse_text :
#     print ("palindrome")
#   else :
#     print("not")
#   return reverse_text
  
# palindrome("madam")
# # palindrome("madamji")


# def larg_num (a=[]):
#   for i in a:
#     if a[0] > a[1]
      
#   else :
#     print("end")

# larg_num(a=[10, 20, 30])



# print(
#   '''hello
#   I am shubham Bahe
#   recently passed out mca 
#   and now practicing Python  
#   '''
# )

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("i m fine")
engine.runAndWait()