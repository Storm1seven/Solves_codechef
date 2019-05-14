for _ in range(int(input())):
    n=int(input())
    s=input()
    index=[]
    for i in range(1,n):
        if(s[i]==s[0]):
            index.append(i)
    if(not index):
        print(s)
    else:
        s+='--------'
        flag=1
        for i in range(1,index[0]+1):
            if(flag==1):
                for j in index:
                    if(s[i+j]!=s[i]):
                        length=i
                        flag=0
                        break
            else:
                length=i-1
                break
        print(s[0:length])