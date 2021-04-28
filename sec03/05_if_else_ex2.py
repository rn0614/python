what=input("도형입력 1:사각형, 2:삼각형, 3:원")

if what=="1":
    a=int(input("가로 길이 입력 :"))
    b=int(input("세로 길이 입력 :"))
    print("사각형의 면적 : %.1f" % (a*b))

elif what=="2":
    a=int(input("밑변 길이 입력 :"))
    b=int(input("높이 길이 입력 :"))
    print("삼각형의 면적 : %.1f" % (a*b/2))

elif what=="3":
    r=int(input("반지름 길이 입력 :"))
    print("원의 면적 : %.1f" % (3.14*r*r))

