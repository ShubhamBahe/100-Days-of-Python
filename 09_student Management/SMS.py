print("============= Student Management System =============")
print('''
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Topper
7. Exit''')


# ================= students data =================== #
student_data = {
  "101" :{
    "name" : "shubham",
    "marks" : 85
  },

  "102":{
    "name" : "vaishi",
    "marks": 86
  },

  "103":{
    "name" : "shuvi",
    "marks": 83
  }
}

# ============== ADD Students =============== #
def ADDSTUDENT():
  student = input("enter student roll no. ")

  if student in student_data :
    print ("student already exist")
  else :
    name = input("enter name of student :")
    marks = int(input("enter marks of student :"))
    if marks <= 0 or marks > 100 :
      print ("marks should not be valid")
    else:
      student_data[student] = {
        "name" : name,
        "marks": marks
      }
      print("Data Add Successfully")

# =============== VIEW STUDENT DATA ============== #

def VIEWDATA():
  for rollno in student_data:
    print("Roll No :", rollno)
    print("Name    :", student_data[rollno]["name"])
    print("Marks   :", student_data[rollno]["marks"])
    print("-" * 25)
    

# =============== SEARCH STUDENT DATA ============== #

def SEARCH_STUDENT():
  rollno = input("Enter the name of student :")
  if rollno in student_data :
      student = student_data[rollno]
      print("Name :", student["name"])
      print("Marks:", student["marks"])
  else:
    print("Student Not Found")

# =============== UPDATE STUDENT DATA ============== #

def UPDATE_DATA():
  urollno = input("enter roll no to update :")
  if urollno in student_data :
    student = student_data[urollno]
    marks = int(input("Enter Marks to update"))
    if marks <= 0 or marks > 100 :
      print ("Please Enter Valid Marks")
    else :
      student["marks"] = marks

      print("NAME :", student["name"])
      print("NEW MARKS :", student["marks"])
  else : 
    print("Student Not Exist")



def DELETE_DATA():
  rollno = input("Enter Roll no to delete data :")
  if rollno in student_data :
    student_data.pop(rollno)
    print("delete data suceesfully")
  else:
    print("Student Not Found")
def TOPPER():
  topname = ""
  toprollno = ""
  topmarks = 0

  for rollno, data in student_data.items():
    if data["marks"] > topmarks :
      toprollno = rollno
      topmarks = data["marks"]
      topname = data["name"]
  print("======== 🏆 Toppers Detail ==========")
  print("TOPER ROLL No. :", toprollno)
  print("TOPER NAME :", topname)
  print("TOPER MARKS :", topmarks)



while True:
  user_input = int(input("Enter input as per Menu :"))
  if user_input == 1:
    ADDSTUDENT()
  elif user_input == 2:
    VIEWDATA()
  elif user_input == 3:
    SEARCH_STUDENT()
  elif user_input == 4:
    UPDATE_DATA()
  elif user_input == 5:
    DELETE_DATA()
  elif user_input == 6:
    TOPPER()
  elif user_input == 7 :
    print("Thank You")
    break
  else :
    print("enter Valid Input")