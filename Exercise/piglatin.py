###Q3 -1 Grading Tag

name = input("Enter your name : ")

name_list=name.split()
i=0

while(i<len(name_list)):
	name_list[i] = name_list[i][1:] + name_list[i][0].lower() + 'ay'
	name_list[i] = name_list[i].capitalize()
	i+=1

new_name = ""
i=0

while (i<len(name_list)):
	new_name+=name_list[i]
	new_name+=" "
	i+=1

print(new_name)