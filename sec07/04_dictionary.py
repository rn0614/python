scores={'kor':90, 'eng':88, 'math':95}

print(scores)

scores["kor"]=100

print(scores)


person3=dict(zip(['이름','키','몸무게'],['성춘향',106,50]))


print(person3.keys())
print(person3.values())
print(person3.items())

to_list=list(person3.keys())
print(to_list)

for key in person3.keys():
    print(key)
