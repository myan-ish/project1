import itertools
player_choice = itertools.cycle([1,2])

game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

#win
def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False
#row winner
	for row in game:
		print(row)
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally!")
			return True

#column win
	for col in range(len(game[0])):
		check = []

		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f"Player {check[0]} is the winner vertically!")
			return True

#diag win
	diags= []
	for id in range(len(game)):
		diags.append(game[id][id])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally!")
		return True

	diags=[]
	for ind, reverse_ind in enumerate(reversed(range(len(game)))):
		diags.append(game[ind][reverse_ind])
	
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally!")
		return True

	return False



#Error handeling
def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("Positon is occupied")
			return game_map, False
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("Error: did  you input row/column as 0, 1 or 2?", e)
		return game_map, False

	except Exception as e:
		print("something went wrong!", e)
		return game_map, False



#Input
play = True
players =[1, 2]
while play:
	game = [[0,0,0],
			[0,0,0],
			[0,0,0]]
	game_won = False
	game, _ = game_board(game, just_display=True)
	
	while not game_won:
		current_player = next(player_choice)
		print(f"Player: {current_player}")
		played = False


		while not played:
			col_choice = int(input("Choose column (0, 1, 2): "))
			row_choice = int(input("Choose row (0, 1, 2): "))
			game, played = game_board(game, current_player, col_choice, row_choice)
			
			if win(game):
				played = True
				game_won : True
				again = input("Again? (y/n) ")
				if again.lower() == "y":
					print("Okay")
				elif again.lower() == "n":
					print("Bye")
					play = False
				else:
					print("Not a valid answer")
					play = False
#play again

if win(game):
    played = True
    game_won : True
    again = input("Again? (y/n) ")
    if again.lower() == "y":
        print("Okay")
    elif again.lower() == "n":
        print("Bye")
        play = False
    else:
        print("Not a valid answer")
        play = False