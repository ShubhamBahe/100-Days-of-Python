while(True):
  A = int(input("Enter First Number to Calculate :"))
  C = input("Enter Your Choice for calculation '+' '-' '*' '/' '%' :")
  B = int(input("Enter Second Number to Calculate :"))

  if(C == "+"):
    print(A+B)
  elif(C == "-"):
    print(A-B)
  elif(C == "*"):
    print(A*B)
  elif(C == "/"):
    if B != 0:
      print(A/B)
    else:
      print("cannot divide by zero")
  elif(C == "%"):
    if B != 0:
        print(A % B)
    else:
        print("Cannot divide by zero.")
  else:
    print("Invalid Input")

  ABC = input("Do you want another calculation? (Y/N) :").upper()
  if (ABC == "N"):
    print("Thank you")
    break
  elif ABC == "Y":
      continue
  else:
      print("Please enter Y or N.")