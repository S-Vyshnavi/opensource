A,B,C=map(int,input().split())
time_req=A*B
avail_time=C*24*60
if time_req<=avail_time:
    print("YES")
else:
    print("NO")
