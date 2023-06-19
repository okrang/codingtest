n,m=map(int,input().split(':'))

numbers=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

mineffort=100
answerhour=''
answerminute=''
def effort(a,b):
    #a에서 b까지의 x와 y의 차이 절댓값을 더한것

    return abs(a[0]-b[0])+abs(a[1]-b[1])
hours=[n]
minutes=[m]

while True:
    hours.append(hours[-1]+24)
    if(hours[-1]>=100):
        hours.pop(-1)
        break

while True:
    minutes.append(minutes[-1]+60)
    if(minutes[-1]>=100):
        minutes.pop(-1)
        break

for i in range(len(hours)):
    for j in range(len(minutes)):
        hour1=hours[i]//10
        hour2=hours[i]%10
        minute1=minutes[j]//10
        minute2=minutes[j]%10
        num=effort(numbers[hour1],numbers[hour2])+effort(numbers[hour2],numbers[minute1])+effort(numbers[minute1],numbers[minute2])
        if(num<mineffort):
            mineffort=num
            answerhour=str(hours[i])
            answerminute=str(minutes[j])
            
            if(hours[i]<10):
                answerhour='0'+answerhour
            if(minutes[j]<10):
                answerminute='0'+answerminute

           

print("{}:{}".format(answerhour,answerminute))
