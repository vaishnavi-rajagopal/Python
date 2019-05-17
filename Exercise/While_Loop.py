string_list = ["apple", "jax", "kitten", "penguin", "snowwoman", "apple"]

x=len(string_list)

while (x>0):
    y=len(string_list[x-1])
    print(string_list.pop(), end=" ")
    print(y)
    x=x-1