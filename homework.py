from random import *

mylist=list()
mylist.append("가위")
mylist.append("바위")
mylist.append("보")

while True:
    i=randint(0,2)
    print(i)
    strInput=input("가위바위보를 입력해주세요")
    print(mylist[i])
    
    if strInput=="가위":
        if  mylist[i]=="바위":
            print("졌습니다.")
        elif mylist[i]=="보":
            print("이겼습니다.")
        else:
            print("비겼습니다.")
    elif strInput=="바위":
        if  mylist[i]=="바위":
            print("비겼습니다.")
        elif mylist[i]=="보":
            print("졌습니다.")
        else:
            print("이겼습니다.")
    elif strInput=="보":
        if  mylist[i]=="바위":
            print("이겼습니다.")
        elif mylist[i]=="보":
            print("비겼습니다.")
        else:
            print("졌습니다.")
    elif strInput=="exit":
        print("종료")
    else:
        print("잘못된 값을 입력했습니다.")
