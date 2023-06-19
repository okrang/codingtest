arrlist=[int(input()) for _ in range(10)]
tmp=0
answer=0
for i in range(len(arrlist)):
    answer+=arrlist[i]
    if(answer==100):
        break
    if answer>100:
        if(abs(tmp-100)>=abs(answer-100)):
            break
        elif(abs(tmp-100)<abs(answer-100)):
            answer=tmp
            break

    else:
        tmp+=arrlist[i]

print(answer)        