N=int(input())
arr=list(map(int,input().split()))
A=int(input())
for i in range(N):
    for j in range(i+1,N):
        if arr[i]+arr[j]==A:
            print("true")
            exit()
print("false")
