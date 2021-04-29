def show_hello():
    print("hello")

show_hello()

def sum():
    a=int(input("숫자1 :"))
    b=int(input("숫자2 :"))
    return a+b

total=sum()
print(total)

def multi_retrun():
    return 1,2,3

a,b,c=multi_retrun()