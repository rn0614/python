money=int(input("교환할 돈은 얼마입니까?"))

coin500= money//500
money%=500

coin100 = money//100
money%=100

coin50= money//50
money%=50

coin10= money //10
money%=10

print("\n오백원짜리 : %d 개" %coin500)
print("\n백원짜리 : %d 개" %coin100)
print("\n오십원짜리 : %d 개" %coin50)
print("\n십원짜리 : %d 개" %coin100)
print("\바꾸지 못한 잔돈 : %d 원" %money)
