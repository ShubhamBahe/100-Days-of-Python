# try :
#   num = int(input("Enter a number: "));
#   print(10 / num);
# except ValueError :
#   print("enter valid no.");
# except ZeroDivisionError:
#   print("not divide by 0");

# a = int(input("enter number 1 "))
# b = int(input("enter number 2 "))

# sum = a+b;
# print (sum);

# A, B = "2", 3
# txt = "@"
# sum = (A + txt);
# final = (sum * B);
# print(sum);
# print(type(sum));
# print(final);
# print(type(final));


# color = input("choose color ")

# if(color == "red"):
#   print("stop");
# elif(color == "yellow"):
#   print("go slow")
# elif(color == "green"):
#   print("go")
# else:
#   print("invalid color")

# marks = int(input("choose marks "))

# if(marks <= 100 and marks >= 90):  
#   print("Grade A")
# elif(marks <= 89 and marks >=80):
#   print("grade B")
# elif(marks <= 79 and marks >=60):
#   print("grade C")
# else :
#   print("fail")


# name = input("enter your name: ")
# print(name,len(name))

# str = "i am $shubham and i love $ symbol"

# print(str.count("a"))
# print(str.replace("shubham", "vaishnavi"));
# print(str.find("v"))
# print(str.capitalize())

# num = 78

# if(num % 7 == 0):
#   print("multiple of 7")
# else:
#   print("not")

# students = ['shubham', 'vaishi', 'raghu', 'rokda']

# print(type(students))
# print(students)
# print(students[0])
# print(students[3])
# print(students[1])
# students[1] = "raja";
# print(students)

# marks = [88, 74, 58, 96, 72, 55, 58]

# marks.append(22)
# marks.sort();
# marks.sort(reverse = True);
# marks.reverse();
# marks.insert(2, 35)
# marks.remove(58)
# marks.pop(3)
# # marks = marks.append(22)
# print(marks)



# FavMovie1 = input("enter you fav movie :")
# FavMovie2 = input("enter you fav movie :")
# FavMovie3 = input("enter you fav movie :")

# FavMovies = [FavMovie1, FavMovie2, FavMovie3]
# print(FavMovies);
# print(type(FavMovies));

# list = [1, 2, 3, 2, 1]
# rev = list.copy()
# rev.reverse()
# if(list == rev):
#   print('palindrome')
# else : 
#   print("not")

# count = 1
# while count <= 100:
#   print(count);
#   count += 1

# n = int(input("table no :"))

# i = 1 
# while i <= 10 :
#   print (i * n)
#   i += 1


# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(numbers):
#   print(numbers[i])
#   i += 1

 
# li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for ch in li: 
#   if(ch == 4):
#     print("4 found")
#   else :
#     print(ch)


# li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for ch in li:
#   if(ch == 9):
#     print(ch, "found")
#   else:
#     print(ch)


# i = 3
# j = 1
# for j  in range (j, 11):
#   print(j*i)


# n = 5
# i = 0
# while i <= n: 
#   print(i)
#   i += n

# i = 10

# sum = 0
# for n in range(1, i+1):
#   sum += n
#   continue
# print(sum)

# i = 1
# sum = 0
# n = 10
# while i <= n:
#   sum += i
#   i += 1
# print(sum)

# n = 5
# fact = 1
# sum = 0
# for i in range(n, fact):
#   fact*=n
# print(fact)

# i = 1
# sum = 1
# num = 5
# while i <= num:
#   sum*=i
#   i+= 1
# print(sum)

# i = 1
# sum = 1
# num = 5
# for i in range(sum, num+1):
#   sum*= i
#   i += 1
# print(sum)

# fact = 1
# num = 5

# def avg(a, b, c):
#   sum = a+b+c
#   ram = sum/3
#   return ram;

# print(avg( 15, 30, 60))


# def sum(a, b):
#   print(a+b)
#   return (a+b)

# sum(2, 2) 

# Marks = [94, 93, 89, 74, 96]

# print(Marks)
# print(type(Marks))
# print(len(Marks))

# def Lists (a = []):
#   print (len(a))
#   return a

# Lists([94, 93, 89, 74, 96])


# def Lists (a = []):
#   print (a)
#   return a

# Lists([94, 93, 89, 74, 96])

# fact = 1
# num = 6
# for i in range(1, num+1):
#   fact *= i
# print(fact)

# def factorial(num):
#   fact=1
#   for i in range (1, num+1):
#     fact *= i
#   print(fact)
#   return fact
  

# factorial(5)
# factorial(6)
# factorial(3)
# factorial(8)


# def Number(a):
#   if (a % 2 == 0):
#     print(a, "number is even")
#   elif(a % 2 != 0):
#     print(a, "number is odd")
#   else :
#     print("invalid input")

# Number(2)
# Number(3)
# Number(4)
# Number(5)
# Number(6)

# def factorial(n):
#   if(n == 0 or n == 1):
#     return 1
#   else :
#     return n * factorial(n-1)    
  
# print(factorial(5))

# def number(n):
#   if(n == 0):
#     return 0
#   return number(n-1) + n

# sum = number(10) 
# print(sum)

# def Rev_num (n):
#   if (n == 0):
#     return 0
#   # print (n)
#   return Rev_num(n-1) + n

# sum = Rev_num(10)
# print(sum)

# def fact(n):
#   if (n==0 or n==1):
#     return 1
#   else :
#     return n * fact(n-1)

# print(fact(5))

# def power(a, b):
#   if (b == 0 or b == 1):
#     return a
#   return a * power(a, b-1)

# print(power(5, 2))

# def num (n):
#   if(n == 0):
#     return 0
#   return num(n-1) + n

# sum = num(5)
# print (sum)

# def Rev_num (n):
#   if (n == 0):
#     return 0
#   # print (n)
#   return Rev_num(n-1) + n

# sum = Rev_num(10)
# print(sum)

# def list(a, idx):
#   if(idx == len(a)):
#     return
#   else:
#     print(a[idx])
#     list(a, idx+1)
  
# list ([10, 20, 30, 40, 50], 0)

# def str_char(a, idx):
#   if idx == len(a):
#     return
#   else:
#     print(a[idx])
#     str_char(a, idx+1)

# str_char ([10, 20, 30, 40, 50], 0)








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


