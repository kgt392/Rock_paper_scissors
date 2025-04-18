import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Score_user = 0
score_cmp = 0
while True:
  list = [rock,paper,scissors]
  user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. enter 4 to exit : "))
  if user > 2 and user != 4 :
    print("entered number  is not between 0 and 2")  
    break
  if user == 4 :
    print("Game END") 
    break
    
  user_choice = list[user]
  print(user_choice)

  cmp = random.choice(list)
  print("Computer choice :")
  print(cmp)

  if (user_choice == rock and cmp == paper) or (user_choice == paper and cmp == scissors) or  (user_choice == scissors and cmp == rock):
    print("You Loss")
    score_cmp += 1
  elif(user_choice == paper and cmp == rock) or (user_choice == scissors and cmp == paper) or  (user_choice == rock and cmp == scissors):
    print("You Win")
    Score_user += 1
  elif (user_choice == paper and cmp == paper ) or (user_choice == scissors and cmp == scissors) or  (user_choice == rock and cmp == rock):
    print("Match Draw")


print(f"User score: {Score_user} \nComputer score: {score_cmp}")