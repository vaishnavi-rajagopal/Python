import math

def countingValleys(n, s):
    m = [0]
    cnt = 0
    flag = False
    ctr = 0
    for i in range(n):
        if(s[i]=='U'):
            cnt+=1
        else:
            cnt-=1
        m.append(cnt)

    print (m)

    for i in range(n+1):
        if((m[i-1]==0) & (m[i]<0)):
            flag = True
        if ((flag == True) & (m[i]==0)):
            flag = False
            print("increasing ctr")
            ctr+=1

    return ctr


print(countingValleys(12, 'DDUUDDUDUUUD'))