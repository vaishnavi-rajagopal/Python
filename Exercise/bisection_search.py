epsilon=0.00001
num=input("enter a number: ")

num=float(num)
low=0.0
high=num
x=0.0

while(high-low>=4*epsilon):
	x=(high+low)/2
	if(x**4<num):
		low=x
	else:
		high=x

print("square_root is",x)
print("squareroot is",num**(1/4))