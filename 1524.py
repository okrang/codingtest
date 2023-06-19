n=int(input())
for i in range(n):
    input()
    S,B=map(int,input().split())
    arrS=list(map(int,input().split()))
    arrB=list(map(int,input().split()))
    arrS.sort()
    arrB.sort()
    while True:
        if len(arrB)==0:
            print('S')
            break
        elif len(arrS)==0:
            print('B')
            break

        
        if(arrB[0]<=arrS[0]):
            arrB.pop(0)
        else:
            arrS.pop(0)
        



