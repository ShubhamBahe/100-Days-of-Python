print("=============== QUIZ GAME ===============")

questions = [
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insert()", "D. push()"],
        "answer": "B"
    },
    {
        "question": "What is the output of 5 // 2 ?",
        "options": ["A. 2", "B. 2.5", "C. 3", "D. 2.0"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. catch", "B. try", "C. except", "D. error"],
        "answer": "B"
    },
    {
        "question": "Which function generates random numbers?",
        "options": ["A. random.randint()", "B. math.random()", "C. rand()", "D. number()"],
        "answer": "A"
    },
    {
        "question": "Which collection type cannot be modified after creation?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    }
]


# ============================ EASY LEVEL ======================== #
def easy():
    correct = 0
    wrong = 0 
    score = 0
    for index, q in enumerate (questions, start=1):
       print(f"{index}. {q['question']}")
       
       for option in q["options"]:
        print(f"{option}")

       user_ans = input("Enter your answer A/B/C/D :").upper()
       while user_ans not in ["A", "B", "C", "D"]:
           print("Invalid Choice")
           user_ans = input("Enter your answer A/B/C/D :").upper()

       if user_ans == q["answer"]:
          print("✅ Correct")
          correct += 1
          score += 5
       else:
          print("❌ wrong")
          wrong += 1

    percentage = (correct / len(questions))*100
    if percentage >= 90:
        performance = "Excellent 🎉"
    elif percentage >= 70:
        performance = "Very Good 👍"
    elif percentage >= 50:
        performance = "Good 🙂"
    else:
        performance = "Keep Practicing 💪"    

    print("=========== Final Scorecard ===========")
    print("correct :",correct)
    print("Wrong   :",wrong)
    print("Score   :",score)
    print("percentage :",percentage)
    print("Performance:", performance) 
    print("=======================================")
    


# ============================ MEDIUM LEVEL ====================== #   

def difficult():
    print("""          ****** WARNING..! ******
If you gave two wrong answer you lose the game""")
    print("")
    correct = 0
    wrong = 0 
    score = 0
    
       
    for index, q in enumerate (questions, start=1):
        print(f"{index}. {q['question']}")
        
        for option in q["options"]:
            print(f"{option}")

        user_ans = input("Enter your answer A/B/C/D :").upper()
        while user_ans not in ["A", "B", "C", "D"]:
            print("Invalid Choice")
            user_ans = input("Enter your answer A/B/C/D :").upper()

        if user_ans == q["answer"]:
            print("✅ Correct")
            correct += 1
            score += 5
        else:
            print("❌ wrong")
            wrong += 1

            if wrong == 2:
                print("game over")
                break

    percentage = (correct / len(questions))*100   
    if percentage >= 90:
        performance = "Excellent 🎉"
    elif percentage >= 70:
        performance = "Very Good 👍"
    elif percentage >= 50:
        performance = "Good 🙂"
    else:
        performance = "Keep Practicing 💪"      

    print("=========== Final Scorecard ===========")
    print("correct    :",correct)
    print("Wrong      :",wrong)
    print("Score      :",score)
    print(f"percentage:{percentage}%")
    print("Performance:", performance)   
    print("=======================================")


print("Select Your level")
print("""*****************
1. Easy
2. Difficult """)

user_input = int(input("Enter your choice 1/2 :"))
if user_input == 1:
   easy()

elif user_input == 2:
   difficult()

else :
   print("Invalid Input")