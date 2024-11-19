T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    remaining=A-B+1
    print(remaining)
