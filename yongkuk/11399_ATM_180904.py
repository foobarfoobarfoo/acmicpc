n = int(input())
times = list(map(int,input().split()))
times.sort()

time, total = 0,0
for i in range(n):
    time += times[i]
    total += time
print(total)

