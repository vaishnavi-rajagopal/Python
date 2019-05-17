from game_class.all_class import Player, Card, Deck
import game_class.explain as explain

#Start the Game
explain.start()

player_one = input("Welcome, Please enter a name for Player 1 ")
player_two = input("Welcome, Please enter a name for Player 2 ")
    
plyr1 = Player(player_one)
plyr2 = Player(player_two)

print("")
print("Welcome {0} and {1} to the Battle of the Pokemon Game".format(plyr1.plyr_nm,plyr2.plyr_nm))
print("")

d1 = Deck()
d1.shuffle()

#Deal the cards to the player
plyr1.plyr_crd = d1.deal_cards(3)
plyr2.plyr_crd = d1.deal_cards(3)

#Allow the player to chose his pokemon.
plyr1.choose_pokemon()
plyr2.choose_pokemon()

while ((plyr1.pk_count != 0) and (plyr2.pk_count != 0)):

	#If the HP of the player's current pokemon is > 0, start the turn - else ask the pokemon to choose another pokemon.
	#break if any one of the players pokemon count becomes 0
	if (int(plyr1.plyr_actpk.pk_hp) > 0):
		print("")
		explain.show_options(plyr1,1,plyr2)
		opt = explain.get_move(plyr1)
		opt1 = ('move'+opt)
		explain.play_turn(plyr1,plyr2,opt1)
	else:
		plyr1.pk_count -= 1
		if (plyr1.pk_count > 0):
			plyr1.choose_pokemon()
			explain.move_expl(plyr1.plyr_actpk)
			opt = explain.get_move(plyr1)
			opt1 = ('move'+opt)
			explain.play_turn(plyr1,plyr2,opt1)

	if (int(plyr2.plyr_actpk.pk_hp) > 0 and plyr1.pk_count > 0):
		print("")
		explain.show_options(plyr2,1,plyr1)
		opt = explain.get_move(plyr2)
		opt1 = ('move'+opt)
		explain.play_turn(plyr2,plyr1,opt1)
	elif (int(plyr2.plyr_actpk.pk_hp) <= 0 and plyr1.pk_count > 0):
		plyr2.pk_count -= 1
		if (plyr2.pk_count > 0):
			plyr2.choose_pokemon()
			explain.move_expl(plyr2.plyr_actpk)
			opt = explain.get_move(plyr2)
			opt1 = ('move'+opt)
			explain.play_turn(plyr2,plyr1,opt1)

#check the count and decide the winner
if (plyr1.pk_count == 0 and plyr2.pk_count != 0):
	print("Player {0} wins" .format(plyr2.plyr_nm))
elif (plyr2.pk_count == 0 and plyr1.pk_count != 0):
	print("Player {0} wins" .format(plyr1.plyr_nm))