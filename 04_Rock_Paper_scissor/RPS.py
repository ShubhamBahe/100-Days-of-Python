import random

CHOICES_EMOJIS = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}

print("============= Rock🗿 Paper📄 Scissor✂️ ============")
print("")


Matches = 0
Draw = 0
Cwon = 0
Uwon = 0

while(True):
  user_choice = (input("Enter Choice Rock/Paper/Scissor :")).strip().lower()
  if user_choice not in CHOICES_EMOJIS :
      print("invalid input")
      continue
  
  Matches += 1
  computer_choice = random.choice(list(CHOICES_EMOJIS.keys()))
  print("The Computer Choice is :", computer_choice)

  if (user_choice == computer_choice):
      print("Shitt : Match Draw 🤝")
      Draw += 1

  elif (user_choice=="rock" and computer_choice=="scissor") or \
       (user_choice=="paper" and computer_choice=="rock") or \
       (user_choice=="scissor" and computer_choice=="paper") :
        print("Yes...: You Won The Game")
        Uwon += 1
      
  else :
      print("Ohhh..... You Lose")
      Cwon += 1

  print("")
  print("========================================")
  print("Match Played :", Matches)
  print("You Won      :", Uwon)
  print("Computer Won :", Cwon)
  print("Draws        :", Draw)
  print("========================================")

  play_again = input("Want to play Again : Y/N :").upper()
  if play_again == "N" :
      print("\nThank You for playing! 👋")
      break
  print("")