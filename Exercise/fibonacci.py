###Q3 -4 Grading Tag

fib_inp = input("Enter a number : ")

if (fib_inp.isnumeric()):

	fib_inp=float(fib_inp)
	a=1
	b=1

	print(a)
	print(a)

	while (b<fib_inp):
		c=b+a
		a=b
		b=c
		if (b<=fib_inp):
			print (b)
else:
	print ("Please enter only a number")