
money=10000
i=1
while money>=2000 :
    print("노래를 %d곡 불렀습니다." % i )
    money-=2000
    if money!=0:
        print("현재 %d원 남았습니다." % money)
    else:
        print("잔액이 없습니다. 종료합니다.")
    i+=1

