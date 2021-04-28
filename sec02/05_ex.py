deposit = int(input("예금액 입력 : "))
inRate = float(input("이자율 입력 (%) :"))


interest= int(deposit*inRate/100)
balance=deposit+interest

print("예금액 : 원", format(deposit, ',' ), "원")
print("이자율: %.1f %%" % inRate)
print("예금이자 : %d 원", format(interest, ',' ), "원")
print("잔액 : %d",format(interest, ',' ),"원")

