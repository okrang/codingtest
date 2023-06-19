voca=input()
#print(ord('z'))
length=len(voca)
#0~length-2전까지 그 후부터 length-1

voca1=voca[:-2]
#print(voca1)
minchar='z'
minindex=length


for i in range (len(voca1)):
    if(ord(voca1[i])<ord(minchar)):
        minchar=voca[i]
        minindex=i

print(minindex)
print(minchar)
