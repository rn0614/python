a=int(input("첫번째 수 :"))
b=int(input("두번째 수 :"))
c=int(input("세번째 수 :"))

if (a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)
