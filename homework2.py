import sys

strStart=input("끝말잇기를 시작합시다. (세글자)")

if len(strStart)==3:
    strEnd=strStart[len(strStart)-1]
    word=input(strEnd+"로 시작하는 말은?")  
    
    while True:
        if len(word)==3 and strEnd==word[0]:
            print("정답입니다.")
            strEnd=word[len(word)-1]
            word=input(strEnd+"로 시작하는 말은?")
        else:
            print("틀렸습니다. 종료")
            sys.exit()
else:
    print("틀렸습니다. 종료")
    sys.exit()