a=input("홀길동 입력 :")
b=input("이몽룡 입력 :")

if a=="가위" :
    if b=="가위":
        result="비겼"
    elif b=="바위":
        result="이몽룡이 이겼"
    elif b=="보":
        result="홍길동이 이겼"
    else :
        result=0

if a=="바위" :
    if b=="가위":
        result="홍길동이 이겼"
    elif b=="바위":
        result="비겼"
    elif b=="보":
        result="이몽룡이 이겼"
    else :
        result=0

if a=="보" :
    if b=="가위":
        result="이몽룡이 이겼"
    elif b=="바위":
        result="홍길동이 이겼"
    elif b=="보":
        result="비겼"
    else :
        result=0

if result==0:
    print("제대로 된 값을 입력하세요")
else:
    print(result+"습니다.")
