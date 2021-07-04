## 기본 변수

출력하는 법 : print(변수)

내용 연결 방법 +와 , 

내용1 + 내용2 둘다 str

, 은 달라도됨

## 포매팅

"문자열 %s, %d, %c ,%.1f   " % 인덱스  : 문자열 뒤에 % 인덱스 를 통행 인덱스에 있는 값 출력

print("내용", end=" " ) 내용 끝나고 끝에 end 에 있는 것을 붙임.



변수형태 변환 : int(), str(), float(),

변수형태 확인 : type()

일정한 형태로 변환 : format( 숫자 , ',') : 천단위 , 구분자 사용 --변환후에는 str 형태임



## 사용자가 입력한 값 받기

input("출력 메세지") : str 형태로 받음. 숫자로 쓰려면 int()로 감싸기



## 리스트 사용

for 변수선언 in [리스트] :

​	리스트내부에 하나씩 실행



len(리스트) : 리스트의 길이

- 보통 for i in range(0, len(리스트)) 형식 사용

리스트[인덱스]= 값 출력    -- 인덱스는 0부터 시작

a,b,c,d= 리스트  : 리스트 값 한번에 대입



리스트[첫번째] [두번째] 사용으로 2차원 배열 사용 가능 첫번째가 바깥쪽 리스트

- [-1] 입력시 제일 뒤에 요소



len(리스트) :  리스트 길이 출력 / 보통 for 문에서 반복 횟수에서 자주 사용

리스트.count(요소, 시작, 끝) : 리스트에서 요소 찾기 / 보통 사전에 몇번 반복해야하는지 확인용으로 remove와 함께 사용

리스트.append(요소) : 리스트에 요소 추가 / 위치는 마지막

리스트.insert(위치, 요소) : 리스트에 위치에 요소 추가

리스트.remove(요소) : 요소에 해당되는 값 삭제 없으면 에러 / 중복값 있을 시에 첫 값만 제거/ for문 사용해서 중복값 제거 가능

리스트.pop(요소) : 요소 추출 / 디폴트 값은 마지막 요소

리스트.extend(리스트) : 리스트에 리스트 추가 내부 리스트가 아닌 일반 합쳐진 리스트로 들어감

리스트.sort(reverse=True) : 요소 정렬 reverse=True면 내림차순

- 리스트.sort() 시 본체 정렬
- sorted(리스트) 시 새로운 정렬 리스트 반환 / 본래 리스트는 유지

리스트.index(요소) : 해당 요소의 인덱스 값 반환  / 찾을 문자가 없으면 에러 / 문자열,리스트, 튜플

문자열.find(요소) : 해당 요소의 인덱스 값 반환  / 찾을 문자가 없으면 -1 / 문자열만 사용

리스트[인덱스] : 해당 인덱스의 요소 값 반환



## 랜덤값 생성법

import random

 random. radint

random.randrange(길이) : 0~ 길이 까지의 수 에서 하나 출력

- 어떤 리스트에서 랜덤으로 하나 뽑을 때 random.randrange(len(리스트)) 형태로 사용



## 집합관련 함수

집합={}             set(리스트)			.add(단수의 값)    .update(복수의 리스트)    .remove(요소)

| 합집합   | 교집합          | 차집합        |
| -------- | --------------- | ------------- |
| .union() | .intersection() | .difference() |
| \|       | &               | -             |





딕셔너리={ : }

.keys()   / .values()   /   .items()

딕셔너리[키] = 값   : 값 추가

딕셔너리 = dict(zip([키 리스트], [값 리스트]))



a is b : a와 b가 동일한 객체를 가르키는지 확인법





## IF문

``` python
if 조건문1:
	print("True")
    pass # 넘어가라는 문장
elif 조건문2:
	print("elif")
else:
    print("False")
```



## x가 배열에 있는지 확인(조건문에서)

| in          | not in          |
| ----------- | --------------- |
| x in 리스트 | x not in 리스트 |
| x in 튜플   |                 |
| x in 문자열 |                 |



## while 문

``` python
while 조건문:
    수행할 문장
    break #강제로 빠져나가기
```



## for 문

``` python
for 변수 in range(len(목록)):
    print("%d 번째 %s" %(number+1,목록[변수]))
```



## range

range 사용시 range 객체가 만들어짐

a=range(10)=range(0,10) = 0,1,2,...,9   #마지막 숫자 미포함.



## 함수선언

``` python
def 함수명(매개변수):
    수행문장
    return 반환값

def 함수명(*매개변수): #입력값이 여러개일 때의 함수명
    수행문장

def 함수명(**키워드): #키워드 형태는 a=1,b=2 
    				#내부에서는 dict 형태로 들어감 {'a':1 , 'b'=2}
    수행문장

#결과값이 2개 이상이면 튜플의 형태로 결과값을 반환

def say_myself(name, old, man=True): #초기값은 맨 뒤에넣을 것 
    
add=lambda a,b : a+b
```



## 파일 생성

``` python
f=open("C:/doit/새파일.txt", 'w') #r,w,a 읽기, 쓰기, 추가 모드
data="데이터 입력"
f.write(data) 	# 파일객체의 write() 내장함수
f.close()
```



## 파일 불러오기

```python
f=open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline() 	# 파일객체의 readlin() 내장함수
    if not line: break		# 빈 라인을 만나면 break
    print(line)	
f.close()
```



``` python
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines() # lines는 리스트 ["1 번째 줄입니다.", "2 번째 줄입니다.", ..., "10 번째 줄입니다."]가 된다
for line in lines:
    print(line)
f.close()
```



``` python
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```



## with문

``` python
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# with문은 open과 close를 같이 처리.
```





## Class

```python
class Calculator:		#calculator 객체 생성
    def __init__(self):		# 초기값 지정
        self.result = 0

    def add(self, num):		#
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
```

