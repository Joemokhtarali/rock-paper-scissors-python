import random

print('Rock..')
print('Paper..')
print('Scissors..')

options = ['rock', 'paper', 'scissors']

p1 = input('Make Your Move: ').lower()
option = random.randint(0,2)
computer = options[option]

print(f'Computer picks {computer}')



if p1 == computer:
    print("Draw")
elif p1 == "rock" and computer == "scissors":
    print("You win!")
elif p1 == "paper" and computer == "rock":
    print("You win!")
elif p1 == "scissors" and computer == "paper":
    print("You win!")
else:
    print("Computer wins!")