def function(N):
    n=N*N
    rev=0
    a=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
        a+=r
    if a==N:
        print("Neon Number")
    else:
        print("Not Neon Number")
N=int(input())
function(N)