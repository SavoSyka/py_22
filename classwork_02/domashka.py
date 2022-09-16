with open("../../pythonProject/input.txt", "r", encoding="utf-8") as f:
    a = list(map(lambda x: x.rstrip().split(), f.readlines()))
ball = [0] * len(a)
number = [0] * len(a)
for i in range(len(a)):
    ball[i] = int(a[i][-1])

max_ball = max(ball)
for i in range(len(a)):
    if int(a[i][-1]) == max_ball:
        print(a[i][-2])
print(max_ball)
