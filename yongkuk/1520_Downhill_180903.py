m,n = map(int,input().split())
data = [[] for i in range(m)]
for i in range(m):
    data[i] = list(map(int,input().split()))   
H_table = [[-1]*n for i in range(m)]

def set_H(i,j):
    global H_table, data, m, n
    H = 0
    
    if H_table[i][j]<0:
        x = [1,-1,0,0]
        y = [0,0,1,-1]
        
        for dx,dy in zip(x,y):
            p=i+dx
            q=j+dy
            if (p<0) or (p==m) or (q<0) or (q==n):
                continue

            else:
                if(data[p][q] > data[i][j]):
                    H += set_H(p,q)
                        
        H_table[i][j] = H
            
    return H_table[i][j]

H_table[0][0] = 1
for i in range(m):
    for j in range(n):
        if(H_table[i][j]<0):
            set_H(i,j)

print(H_table[m-1][n-1])


