T=int(input())
for _ in range(0,T):
    A,B=map(int,input().split())
    if A>B:
        print(A-B)
    else:
        print("0")
