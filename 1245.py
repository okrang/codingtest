def dfs(a,b):
    global trigger
    #12시방향부터 시계방향
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[-1,-1,0,1,1,1,0,-1]

    visited[a][b]=True
    for i in range(8):
        x=a+dx[i]
        y=b+dy[i]

        if -1<x<n and -1<y<m:
            if graph[a][b]<graph[x][y]:
                trigger=False
            
            if not visited[x][y] and graph[x][y]==graph[a][b]:
                dfs(x,y)
            



n,m=map(int,input().split())
arrlist=[]
graph=[list(map(int,input().split())) for _ in range(n)]
count=0


visited=[[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]>0 and not visited[i][j]:
            trigger=True
            dfs(i,j)
            if trigger:
                count+=1

print(count)

