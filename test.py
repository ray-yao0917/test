t=int(input())
ans = []
for i in range (t):
    x = input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    if (x[2] - x[1]) == (x[3] - x[2]):
         x.append(x[3]+(x[2] - x[1]))
    elif (x[2] // x[1]) == (x[3] // x[2]):
        x.append(x[3]*(x[2] // x[1]))
    ans.append(x)
for i in ans :
    print(i)