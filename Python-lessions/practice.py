# ============ Question 1 ============= #
# Write a function: that returns the number of digits in an integer.
# def count_digit(num):
#   count = 0
#   while num > 0:
#     num = num // 10
#     count += 1
# #   return count

# # print(count_digit(456785412))


# def rev_num(num):
  
#   reverse = 0
#   while num > 0:
#     num = num % 10
#     reverse = reverse + 
#   return count

# print(rev_num(123))

# =========================== counts the number ======================= #
# def number(num):
#   count = 0
#   while num > 0:
#     num = num // 10
#     count += 1
#   return count

# print(number(1256345588))

# ==================== reverse a number ======================= #
# def rev_number(num):
#   reverse = 0
#   while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#   return reverse

# # print(rev_number(12314785))


# ================= palindrome number if yes return true else false ================== #
# def rev_num(num):
#   orignal = num
#   reverse = 0
#   while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#   if orignal == reverse :
#     return True
#   else:
#     return False  

# print(rev_num(1212))


# =========================== addition of a number ========================= #

# def add_num(num):
#   count = 0
#   while num > 0:
#     digit = num % 10
#     count = count + digit 
#     num = num // 10
#   return count 

# print(add_num(9085))


# ============================ find largest number ================= #
# def large_num(num):
#   largest = 0
#   while num > 0:
#     digit = num % 10
#     if digit > largest:
#       largest = digit 
#     num = num // 10
#   return largest

# print(large_num(123))
    

# ============== find second largest number ================= #
# def second_large(num):
#   largest = 0
#   second_largest = 0
#   while num > 0:
#     digit = num % 10
#     if digit > largest:
#       second_largest = largest
#       largest = digit 
#     elif digit > second_largest :
#       second_largest = digit
#     num = num // 10
#   return second_largest

# print(second_large(123))


# ======== Write a function to check whether a number is prime or not.====== #
# def check_num(num):
#   if num <= 1 :
#     print("not prime")
#   elif num % 2 == 0:
#     print("not prime")
#   else:
#     print("prime")
    

# check_num(1)
# check_num(2)
# check_num(3)
# check_num(4)
# check_num(5)

# # data = {"a": 1, "b": 2, "c": 3}

# # for item in data.items():
# #     print(item)

# # matrix = [[1, 2, 3], 
# #           [4, 5, 6], 
# #           [7, 8, 9]]
# # flat = [num for row in matrix for num in row]
# # print(flat)

# # grid = [[1, 2], [3, 4]]
# # result = [col for row in grid for col in row if col % 2 == 0]
# # print(result)


# # fruits = input("enter seven fruits name :")
# # fruits1 = [fruits]
# # print(fruits1)
# # print(type(fruits1))  


# f1 = 15
# marks = [12, 14, 16, 23, 18]

# marks.insert(1, 11)
# marks.append(f1)
# marks.sort(reverse = True)
# marks.remove(23)
# marks.pop()
# marks.pop()
# marks[0] = 78
# marks[1] = 88
# marks[2] = 89
# marks[3] = 87
# print(marks)

# a = marks.count(78)
# print(a)

# avg = sum(marks)
# print(avg)
# print(avg/len(marks))


# marks = (12, 14, 25, 24, 26, 78)

# marks[0] = 14,
# print(marks)


# for i in range (1, 6):
#   print (i)


# i = 1
# while (i<6):
#   print ("shubham")
#   i += 1

# list = [10, 20, 30, 40, 50]

# i = 0
# while i < len(list):
#   print(list[i])
#   i += 1

# for i in range (len(list)):
#   print (list[i])
#   i += 1

# n = "*"
# for i in range (6, 1):
#   print (n*i)

# lodu = ["shubham", "sakshi", "vaishi", "raju", "bhim", "chutki", "shmajhs"]

# for name in lodu :
#   if(name.startswith("s")):
#     print (f"hello {name}")


# x = 100
# y = x
# z = y

# y = 200

# print(x)
# print(y)
# print(z)

# a = 10
# b = 20

# a = b

# print(a)
# print(b)

# a = 10
# b = "10"

# print(type(a))
# print(type(b))

# print(a == b)

# Num = int(input("Enter a Number :"))
# for i in range (1, Num+1):
#   print(" " * (Num-i),end="")
#   print("*" * (2*i-1),end="")
#   print("")
  
Num = int(input("Enter a Number :"))
for i in range(1, Num+1):
  print(" "* (Num-i) + "*" * (2*i-1))