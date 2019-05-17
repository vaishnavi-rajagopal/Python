###Q3 -2 Grading Tag

matrix_inp = input("Please enter four numbers seperated by spaces : ")
matrix_list=matrix_inp.split()

if(len(matrix_list)==4):
	a=float(matrix_list[0])
	b=float(matrix_list[1])
	c=float(matrix_list[2])
	d=float(matrix_list[3])

	matrix_tup=((a,b),(c,d))
	print("Matrix:"+ str(matrix_tup))

	x=(1/((a*d)-(b*c)))
	a1=d*x
	b1=-b*x
	c1=-c*x
	d1=a*x
	inverse_tup=((a1,b1),(c1,d1))
	print("Inverse:"+str(inverse_tup))
else:
	print("Please enter 4 numbers seperated by spaces")