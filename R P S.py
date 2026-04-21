import random

rock = '''
_      ___ ___
|  _,-' _ `\__)
|~'    '(_____) 
|       (____)
|      (_____)
|--.____(___)
'''

papper = '''               
               _  / |
              / \ | | /
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |'''

siccors = ''' 
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/  '''

game_images = [rock,papper,siccors]

player1 = int(input("Choose 0 for rock or 1 for paper or 2 for siccors: "))

if player1 >= 0 and player1 <= 3:
    print(game_images[player1])
computer_choice = random.randint(0,2)

print("computer Choose:")
print(game_images[computer_choice])

if player1 >= 3:
    print("you enter invalid number you lose!")
elif player1 == computer_choice:
    print("Draw")
elif player1 == 2 and computer_choice == 0:
    print("you lose!")
elif player1 > computer_choice:
    print("you win!")
elif player1 == 0 and computer_choice == 2:
    print("you win!")
elif player1 < computer_choice:
    print("you lose!")

