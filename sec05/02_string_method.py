cities ="인천 대전 광주 울산 대구 부산"

city =input("도시 입력 :")

if cities.find(city) !=-1:
    print("존재합니다.")
else:
    print("없습니다.")

email= input("이메일을 입력하세요")
if (email.find("@")!=-1) and (email.find(".")!=-1) and(email.find("@")<email.find(".")):
    print("입력한 이메일 : %s" % email)
else:
    print("이메일 형식이 아닙니다.")


alphas=digits=spaces=others=0

string=input("문장을 입력하세요 : ")

for c in string:
    if c.isalpha():
        alphas+=1
    elif c.isdigit():
        digits+=1
    elif c.isspace():
        spaces+=1
    else:
        others+=1

print("알파벳 : %d개" %alphas)
print("숫자 : %d개" %digits)
print("스페이스 : %d개" %spaces)
print("기타 : %d개" %others)


