i,r,k=map(int,input().split())
s=0
for i in range(i,r+1):
    if i%k==0:
        s+=1
print(s)