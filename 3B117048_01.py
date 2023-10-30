starNum=int(input("請輸入星星數量:"))
space=int(starNum/2)
for i in range(1,starNum+1,2):
    print(" "*space+"*"*i)
    space-=1
space=1
for i in range(starNum,0,-2):
    if(starNum!=i):
        print(" "*space+"*"*i)
        space+=1