
year1=input("Enter your birth year ")
year1=int(year1)
years_list=[year1]

for i in range(1,5):
	year1=year1+1
	years_list.append(year1)

print(years_list)
print(years_list[3])
print(max(years_list)) 