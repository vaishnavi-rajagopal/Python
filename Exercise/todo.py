###Q3 -3 Grading Tag
act_inp = "start"
to_do={"monday":[],"tuesday":[],"wednesday":[],"thursday":[],"friday":[],"saturday":[],"sunday:[]"}

while(act_inp!="quit"):

	act_inp=input("What would you like to do? add, get, quit ?")

	if (act_inp=="add"):

		day_inp=input("What day?")
		day_inp=day_inp.lower()
		
		if (day_inp in to_do):
			item_inp=input("What would you like to add to " + day_inp + " to-do list?")
			to_do[day_inp].append(item_inp)

		else:
			print("Invalid entry - please enter a correct day of the week (like Monday or monday)")

	elif (act_inp=="get"):

		day_inp=input("What day?")
		day_inp=day_inp.lower()
		print("You have to ", end="")
		i=0
		while(i<len(to_do[day_inp])):
			print (to_do[day_inp][i], end="")
			i+=1
			if (i<len(to_do[day_inp])):
				print (" and ", end="")
		print("")
	elif (act_inp=="quit"):
		print("Ending program. Thank you for using the to-do list!")

	else:
		print("Enter either 'add' or 'get' or 'quit'")