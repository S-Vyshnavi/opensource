A,B,C=map(int,input().split())
if C<A:
    print("0")
elif C<(A+B):
    print("1")
else:
    print("2")
