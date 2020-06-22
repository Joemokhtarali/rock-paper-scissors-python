print('Rock..')
print('Paper..')
print('Scissors..')

player1 = input('Player1, make your move: ')
player2 = input('Player2, make your move: ')

if player1 == 'rock' and player2 == 'scissors':
	print('Player1 wins')

elif player1 == 'scissors' and player2 == 'paper':
	print('Player1 wins')

elif player1 == 'paper' and player2 == 'rock':
	print('Player1 wins')

elif player2 == 'rock' and player1 == 'scissors':
	print('player2 wins')

elif player2 == 'rock' and player1 == 'scissors':
	print('player2 wins')

elif player2 == 'rock' and player1 == 'scissors':
	print('player2 wins')