name=input()
nameL=name.count('L')
nameO=name.count('O')
nameV=name.count('V')
nameE=name.count('E')
num=int(input())
maxpercent=0
victeam=''
arrlist=[]
for i in range(num):
    teamname=input()
    varL=teamname.count('L')+nameL
    varO=teamname.count('O')+nameO
    varV=teamname.count('V')+nameV
    varE=teamname.count('E')+nameE
    percent=((varL+varO)*(varL+varV)*(varL+varE)*(varO+varV)*(varO+varE)*(varV+varE))%100
    print(percent)
    if percent>=maxpercent:
        maxpercent=percent
        victeam=teamname
    
   # print(victeam)
    arrlist.append(teamname)

if(maxpercent==0):
    arrlist.sort()
    print(arrlist[0])
else:
    print(victeam)






