import sys

meetings = []
n = int(sys.stdin.readline())

i=0
while i < n:
    meetings.append(tuple(map(int,sys.stdin.readline().split())))
    i += 1

meetings.sort(key=lambda x:(x[1],x[0]))

count = 0
end = 0

i=0
while i < n:
    if(end<=meetings[i][0]):
        end = meetings[i][1]
        count += 1
    i += 1
        
print(count)

