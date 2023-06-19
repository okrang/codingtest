n,m=map(int,input().split())
#print(n)
#print(m)

arrlist=[]

for i in range(n):
    tmparr=input()
    tmplist=[]
    for j in range(m):
        tmplist.append(tmparr[j])
    arrlist.append(tmplist)
#print(arrlist)

rowcount=0
for i in range (n):
    if 'X' not in arrlist[i]:
        rowcount+=1

colcount=0
#print([i[0] for i in arrlist])
for i in range(m):
    if 'X' not in [j[i] for j in arrlist]:
        colcount+=1

print(max(colcount,rowcount))




