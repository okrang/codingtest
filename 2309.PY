
arrlist=[]
for i in range(9):
    arrlist.append(int(input()))

arrlist.sort()
sumheight=sum(arrlist)

for i in range(9):
    for j in range(i+1,9):
        if(sumheight-arrlist[i]-arrlist[j]==100):
            arrlist.pop(i)
            arrlist.pop(j-1)
            for k in range(len(arrlist)):
                print(arrlist[k])
            exit()

