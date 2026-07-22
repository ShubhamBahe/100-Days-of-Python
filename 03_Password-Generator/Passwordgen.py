import random

print("============= Welcome to Password Generator =============")
print("=============== Thank you For Choosing Us ===============")
print("")


passlen = int(input("Enter the length of Password :"))

upprcse = input("Want to Enter Uppercase in your Password: Y/N :").upper()
lwercse = input("Want to Enter Uppercase in your Password: Y/N :").upper()
number  = input("Want to Enter Uppercase in your Password: Y/N :").upper()
symbols = input("Want to Enter Uppercase in your Password: Y/N :").upper()

char  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lchar = "abcdefghijklmnopqrstucwxyz"
num   = "1234567890"
sym   = "!@#$%^&*()_+-=[]|;:,.<>?"

words = ""

if upprcse == "Y":
  words += char
if lwercse == "Y":
  words += lchar
if number == "Y":
  words += num
if symbols == "Y":
  words += sym

if words == "":
  print("\nError: Please select at least one character type!")
else :
  password = ""
  for _ in range(passlen):
   password += random.choice(words)

  print(password)
