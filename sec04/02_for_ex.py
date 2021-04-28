a=["홍길동","이몽룡","성춘향","변학도"]

b=input("이름 입력 : ")

for i in a:
    if b==i:
        find=True
        break
    else:
        find=False

if find==True:
    print("명단에 없습니다.")
else:
    print("명단에 없습니다")