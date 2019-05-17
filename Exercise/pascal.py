###Q3 -5 Grading Tag
n=input("Enter a row number: ")

if(n.isnumeric()):
      n=int(n)
      pscl_trngl={}

      i=1
      while(i<n+1):
            pscl_trngl[i] = [1]*i
            i+=1

      j=3
      base_list=pscl_trngl[2]
      while (j>2 and j<n+1):
            list_val=pscl_trngl[j]

            k=1
            while(k<len(list_val)-1):
                  list_val[k]=base_list[k-1]+base_list[k]
                  k+=1
            base_list=list_val
            pscl_trngl[j]=list_val
            j+=1

      print(pscl_trngl[n])
else:
      print("Please enter a number value for the row")