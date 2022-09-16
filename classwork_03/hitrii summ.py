m = int(input())
b = list(set(map(int, input().split())))
for i in range (len(b)-1):
    for j in range (i+1,len(b)):
        if b[i]+b[j]==m:

            print(b[i],b[j])
