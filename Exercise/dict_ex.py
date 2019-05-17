string_inp = input("Enter a bunch of words to count: ")

string_inp=string_inp.lower()
string_list = string_inp.split()

count_dict = {}

while (len(string_list))>0:
    word_list = (string_list.pop())
    if (word_list in count_dict):
        count_dict[word_list]+=1
    else:
        count_dict[word_list]=1
        
print(count_dict)