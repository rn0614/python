dict={}

while True:
    a=input("영어단어 등록(종료는 quit) : ")



    if a==quit:
        break
    elif a in dict:
        print("%s는 이미 등록된 단어입니다." % a)
    else:
        b = input("%s의 뜻입력(종료는 quit)" % a)
        dict[a] = b

while True:
    a=input("검색할 단어 입력")

    if a==quit:
        break
    if a in dict:
        print("%s의 뜻은 %s입니다." % (a,dict[a]))
    else:
        print("%s는 사전에 없는 뜻입니다." % a)

print("\n 종료합니다.")