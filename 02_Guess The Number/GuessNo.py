import random
num = random.randint(1, 100)
attempt = 0
GamePlayed = 0
GameWon = 0
best_score = None

while(True):
  
  if(attempt >= 7):
    GamePlayed += 1
    print("Game Over")
    print("The Number Was", num)
    break

  else:
    UserInput = int(input("Guess the Number :"))
    attempt += 1

  if(UserInput == num):
      GameWon += 1
      GamePlayed += 1

      if best_score is None or attempt < best_score:
        best_score = attempt

      print("Congratulation, you guess the correct number")
      print(f"you guess number in {attempt} attempts")


      print("========== Statistics ==========")
      print("Game Played :", GamePlayed)
      print("Game Won    :", GameWon)
      print("Best Score  :", best_score)
      print("================================")
            
      

      PlayAgain = input("Want to play Again? Y/N : ").upper()
      if PlayAgain == "N":
          print("thank you for playing")
          break
      elif PlayAgain == "Y":
          num = random.randint(1, 100)
          attempt = 0
          continue

  elif(UserInput < num):
    print("Your Number is less.")
    print(f"Your Number of Current Attempt is : {attempt}")

  elif(UserInput > num):
    print("Your Number is Big.")
    print(f"Your Number of Current Attempt is : {attempt}")
   