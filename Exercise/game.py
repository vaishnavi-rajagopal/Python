from game_class.all_class import Player, Card, Deck
import game_class.explain as explain

def choose_pokemon(plyr):
	global choice
	if (len(plyr.plyr_crd) > 1 ):
		print("Player {0} - Your Pokemon's are - {1}" .format(plyr.plyr_nm,plyr.plyr_crd))
		print("Your Pokemon Details are as below.")
		explain.sepr(len("Your Pokemon Details are as below."))
		for i in range(len(plyr.plyr_crd)):
			explain.poke_expl(plyr.plyr_crd[i])
		ap = input("Please choose your active pokemon - ")
		plyr.set_actpk(Card('P',ap))
		plyr.rem_actpk(ap)
	else :
		ap = str(plyr.plyr_crd[0].crd_nm)
		plyr.set_actpk(Card('P',ap))
		print("Player {0} - Your active Pokemon is {1}" .format(plyr.plyr_nm,plyr.plyr_actpk.crd_nm))
		plyr.rem_actpk(ap)

def play_turn(plyr1,plyr2,mv):
	mv_hp = str(mv)+'_hp'
	print("{0} played {1} on {2} and caused a damage of {3}" .format(plyr1.plyr_actpk.crd_nm,plyr1.plyr_actpk.get_char(mv),plyr2.plyr_actpk.crd_nm,plyr1.plyr_actpk.get_char(mv_hp)))
	plyr2.plyr_actpk.pk_hp = int(plyr2.plyr_actpk.get_char('hp')) - int(plyr1.plyr_actpk.get_char(mv_hp))
	print("Player {0} - Active Pokemon is {1} Balance HP is {2}" .format(plyr2.plyr_nm,plyr2.plyr_actpk.crd_nm,plyr2.plyr_actpk.pk_hp))

explain.start()
g = input("Do you want to start the game. Press Y/N.")
if (g.upper() == 'Y'):
	print ("Starting Game")
elif (g.upper() == 'N') :
	print ("See you again, Quitting the game")
else :
	print ("Please enter only Y or N")

player_one = input("Welcome, Please enter a name for Player 1 ")
player_two = input("Welcome, Please enter a name for Player 2 ")
    
plyr1 = Player(player_one)
plyr2 = Player(player_two)

print("")
print("Welcome {0} and {1} to the Battle of the Pokemon Game".format(plyr1.plyr_nm,plyr2.plyr_nm))

d1 = Deck()
d1.shuffle()

plyr1.plyr_crd = d1.deal_cards(3)
plyr2.plyr_crd = d1.deal_cards(3)

choose_pokemon(plyr1)
choose_pokemon(plyr2)

repeat = 1
while(repeat == 1):
	repeat = explain.options(plyr1)

repeat = 1
while(repeat == 1):
	repeat = explain.options(plyr2)

while ((plyr1.pk_count != 0) and (plyr2.pk_count != 0)):
	print(plyr1.pk_count)
	print(plyr2.pk_count)
	if (int(plyr1.plyr_actpk.pk_hp) > 0):
		if ('-' in plyr1.plyr_actpk.pk_mov2):
			opt = input("Player {0} - Do you want to use move1 or move2? " .format(plyr1.plyr_nm))
		else:
			opt = '1'
		if (opt == '1'):
			opt1 = 'move1'
		else:
			opt1 = 'move2'
		play_turn(plyr1,plyr2,opt1)
	else:
		plyr1.pk_count -= 1
		if (plyr1.pk_count > 0):
			choose_pokemon(plyr1)
			explain.move_expl(plyr1.plyr_actpk)
			if ('-' in plyr1.plyr_actpk.pk_mov2):
				opt = input("Player {0} - Do you want to use move1 or move2? " .format(plyr1.plyr_nm))
			else:
				opt = '1'
			if (opt == '1'):
				opt1 = 'move1'
			else:
				opt1 = 'move2'
			play_turn(plyr1,plyr2,opt1)

	if (int(plyr2.plyr_actpk.pk_hp) > 0 and plyr1.pk_count > 0):
		if ('-' in plyr2.plyr_actpk.pk_mov2):
			opt = input("Player {0} - Do you want to use move1 or move2? " .format(plyr2.plyr_nm))
		else:
			opt = '1'
		if (opt == '1'):
			opt1 = 'move1'
		else:
			opt1 = 'move2'
		play_turn(plyr2,plyr1,opt1)
	elif (int(plyr2.plyr_actpk.pk_hp) <= 0 and plyr1.pk_count > 0):
		plyr2.pk_count -= 1
		if (plyr2.pk_count > 0):
			choose_pokemon(plyr2)
			explain.move_expl(plyr2.plyr_actpk)
			if ('-' in plyr2.plyr_actpk.pk_mov2):
				opt = input("Player {0} - Do you want to use move1 or move2? " .format(plyr2.plyr_nm))
			else:
				opt = '1'
			if (opt == '1'):
				opt1 = 'move1'
			else:
				opt1 = 'move2'
			play_turn(plyr2,plyr1,opt1)

if (plyr1.pk_count == 0 and plyr2.pk_count != 0):
	print("Player {0} wins" .format(plyr2.plyr_nm))
elif (plyr2.pk_count == 0 and plyr1.pk_count != 0):
	print("Player {0} wins" .format(plyr1.plyr_nm))