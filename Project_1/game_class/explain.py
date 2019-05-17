def start():
	'''This method is used to list all the initialization instructions'''
	sepr(len("Welcome to the Pokemon Battle Game"))
	print("Welcome to the Pokemon Battle Game")
	sepr(len("Welcome to the Pokemon Battle Game"))
	print("The Rules of the game are as below :")
	print("1. This is a 2 player game.")
	print("2. At the start of the game, the deck will deal 3 pokemon cards and 3 prize cards and 10 deck cards to each of the players.")
	print("3. Pokemon cards are the cards which will be used for the battle, in short your soldiers.")
	print("4. Once the pokemon cards are dealt to each of the players, every player is given an option to choose their active pokemon.")
	print("   You can only have one active pokemon at any time.")
	print("5. Every pokemon has 2 moves based on the type of the pokemon.")
	print("6. The game continues till all the pokemons of a player are captured.")
	print("   The player who captures all the opponent's pokemons first - WIN.")
	print("All The Best !")
	print("")
	inp = 1
	
	while (inp == 1):
		g = input("Do you want to start the game. Press Y/N.")
		if (g.upper() == 'Y'):
			print ("Starting Game")
			sepr(len("Starting Game"))
			print("")
			inp = 0
		elif (g.upper() == 'N') :
			print ("See you again, Quitting the game")
			sepr(len("See you again, Quitting the game"))
			print("")
			inp = 0
			exit()
		else :
			print ("Please enter only Y or N")

def sepr(cnt):
	'''This method is used to print line seperation between sentences'''
	print("*" * cnt)

def validate(val,type,plyr):
	'''This method consolidates all the validation done on the user input.'''
	opt = val
	if(type=='move'):
		if(opt=='1' or opt =='2'):
			return True
		else:
			print("Please enter either 1 or 2 as input")
			return False
	elif(type=='pk_name'):
		ap = val
		for i in range(len(plyr.plyr_crd)):
			if (str(ap)  == str(plyr.plyr_crd[i])):
				a = 1
				break
			else:
				a = 0
		if (a==0):
			print("Please chose a value within the list of pokemons above")
			return False
		else:
			return True

def move_expl(p_crd):
	'''This method displays the move explanation for each pokemon'''
	print("{0} Move Details as below" .format(p_crd.crd_nm.title()))
	mv1 = str(p_crd.pk_mov1).split('-')
	if ('-' in p_crd.pk_mov2):
		mv2 = str(p_crd.pk_mov2).split('-')
	print("Move 1 - {0} and causes damage {1}" .format(str(mv1[0]),str(mv1[1])))
	if ('-' in p_crd.pk_mov2):
		print("Move 2 - {0} and causes damage {1}" .format(str(mv2[0]),str(mv2[1])))

def poke_expl(p_crd):
	'''This method displays all the attributes about a pokemon so as to enable the player to chose the active one'''
	mv1 = str(p_crd.pk_mov1).split('-')
	if ('-' in p_crd.pk_mov2):
		mv2 = str(p_crd.pk_mov2).split('-')
	print("")
	print("Pokemon {0} has the below attributes:" .format(p_crd.crd_nm))
	sepr(len("Pokemon [name] has the below attributes:"))
	print("Name - {0}" .format(p_crd.crd_nm))
	print("Type - {0}" .format(p_crd.pk_type))
	print("HP - {0}" .format(p_crd.pk_hp))
	print("Move 1 - {0} and causes damage {1}" .format(str(mv1[0]),str(mv1[1])))
	if ('-' in p_crd.pk_mov2):
		print("Move 2 - {0} and causes damage {1}" .format(str(mv2[0]),str(mv2[1])))
	#print("Weakness - {0}" .format(p_crd.pk_weakness))

def options(player,player2):
	'''This method displays all the options and implements the flow based on user input'''
	val = 1
	print("")
	print("Player {0} Options" .format(player.plyr_nm.title()))
	sepr(len("Player [Name] Options"))
	print("1. Check Player Status")
	print("2. Check Active Pokemon Move Details")
	print("3. Resign and Exit Game")
	print("4. Exit this menu and Continue the Game")
	option = input("Enter a number for the options as above.")
	if (int(option) == 1):
		print("")
		player.status()
		return val
	elif (int(option) == 2):
		print("")
		move_expl(player.plyr_actpk)
		return val
	elif (int(option) == 3):
		print("")
		print("Player {0} resigns and Player {1} WINS !!" .format(player.plyr_nm,player2.plyr_nm))
		exit()
	elif (int(option) == 4):
		val = 0
		return val
	else:
		print("Please enter a valid option")
		return val

def play_turn(plyr1,plyr2,mv):
	'''This method makes the actual move and displays the move details and resulting HP score.'''
	mv_hp = str(mv)+'_hp'
	print("{0} played {1} on {2} and caused a damage of {3}" .format(plyr1.plyr_actpk.crd_nm,plyr1.plyr_actpk.get_char(mv),plyr2.plyr_actpk.crd_nm,plyr1.plyr_actpk.get_char(mv_hp)))
	plyr2.plyr_actpk.pk_hp = int(plyr2.plyr_actpk.get_char('hp')) - int(plyr1.plyr_actpk.get_char(mv_hp))
	print("Player {0} - Active Pokemon is {1} Balance HP is {2}" .format(plyr2.plyr_nm,plyr2.plyr_actpk.crd_nm,plyr2.plyr_actpk.pk_hp))

def show_options(plyr,x,plyr2):
	'''This method is to show the user options in between the game.'''
	while(x == 1):
		x = options(plyr,plyr2)

def get_move(plyr):
	'''This method receives the user input for the move option'''
	if ('-' in plyr.plyr_actpk.pk_mov2):
			check = False
			while(check == False):
				print("")
				opt = input("Player {0} - Do you want to use move1 or move2? " .format(plyr.plyr_nm))
				check = validate(opt,'move',plyr)
	else:
		opt = '1'
	return opt
