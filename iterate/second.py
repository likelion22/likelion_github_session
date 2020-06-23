# a=int(input("값을 입력하세요 : "))
# if a>0:
#     print("a는 양수입니다.")
#     if a%2==0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
# else:
#     print("a는 음수입니다.")


########## 반복문 ############

# mylist=list()
# mylist=[1,2,3]


# for i in mylist:
#     print(i)
    

# # myrange=range(500,1000,100)
# # for i in myrange:
# #     print(i)
    
# # temp_str="안녕하세요오늘날씨는화창합니다."

# # for i in range(len(temp_str)):
# #     print(temp_str[i],"의 인덱슨는 :", i)


# # b=int(input("반복할 횟 수 : "))

# # def forfunction(a):
# #     for i in range(a):
# #         print(i)

# # forfunction(b)


# # def hellofunction(a):
# #     for i in range(a):
# #         print("Hello"*a)

# # hellofunction(b)

# # def mysum(a,b):
# #     c=a+b
# #     return c

# # print(mysum(5,10))


# for i in [1,2,3,4]:
#     if i == 2:continue #반복문 처음으로 돌아가라
#     print(i)
    
# # a=1
# # while True:
# #     print(a)
# #     a+=1
# #     if(a==100):break


# class NS5:
#     body = "강화합금" #클래스 변수
    
#     def run(self): #메소드 #항상 객체 나 자신이 들어감.
#         print("달립니다", self)
        
# NS5_1=NS5()
# NS5_2=NS5()

# print(type(NS5_1))
# print((NS5_1).body)
# NS5_1.run()

# NS5_2.sense ="Happy"  #객체 변수


# print(NS5_2.sense)



for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j," ", end='')
    print()