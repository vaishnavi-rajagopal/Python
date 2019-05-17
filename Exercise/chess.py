size=input("Enter a board size: ")

if (size.isnumeric()):

	n=int(size)
	board=[[] for x in range(n)]

	for i in range (0,n):
		board[i] = [1 if j==0 else 0 for j in range(0,n)]

	for i in range (1,n):
		board[i] = [(board[i-1][j-1]+board[i-1][j])for j in range(0,n)]

	for i in range (0,n):
		print (board[i])
else:
	print("Please input a valid number")


