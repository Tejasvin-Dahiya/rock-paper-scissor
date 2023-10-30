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

al=[rock,paper,scissors]
random_int=random.randint(0,2)
print("What do you choose?")
choice=int(input("Type 0 for rock, 1 for paper and 2 for scissors"))
if choice==0:
  print("You chose")
  print(rock)
  print("Computer chose:")
  print(al[random_int])
  if random_int==0:
    print("Its a tie")
  elif random_int==1:
    print("You lose")
  else:
    print("You win")
    
elif choice==1:
  print("You chose: Paper")
  print(paper)
  print("Computer chose:")
  print(al[random_int])
  if random_int==0:
    print("You win")
  elif random_int==1:
    print("Its a tie")
  else:
    print("You lose")
else:
  print("You chose: scissors")
  print(scissors)
  print("Computer chose:")
  print(al[random_int])
  if random_int==0:
    print("You lose")
  elif random_int==1:
    print("You win")
  else:
    print("Its a tie")
    