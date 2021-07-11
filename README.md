## print()

출력하는 법 : print( 내용, sep="사잇값", end="끝값")

내용 연결 방법 +와 (,) 둘이 있음.

- +의 경우 sep="" , (,)의 경우 sep=" "을 default 값으로 가짐.
- +의 경우 다른 자료형 사용 불가, (,)은 다른 자료형도 사용 가능

print('a', 1, sep=':', end='.')



## python 내장함수

`len(배열)`, `min(배열)`, `max(배열)`, `pow(값, 제곱수)`, `input(출력문)`, `round(float,소수점 아래 자릿수)`, `list(zip(배열1,배열2))`



## 배열-> 문자열, 문자열-> 배열

`"".join(배열)` : 배열을 문자열로 변환

`문자열.spilt("기준") `: 문자열을 split 안에 있는 것으로 등분



## 문자열 함수

문자열.strip() : 양쪽 공백 제거

문자열.replace( "원래 문자","바꿀 문자") : 문자열에서 원래 문자를 바꿀 문자로 모두 변경

문자열.startswith('문자열1') : 문자열이 문자열1로 시작하는지 확인

문자열.endswith('문자열2') : 문자열이 문자열2로 끝나는지 확인 

문자열.count('문자') : 문자열에서 문자의 숫자 구하기

문자열.index('문자', 시작위치) : 문자열에서 문자 위치 찾기

문자열.find('문자', 시작위치) :문자열에서 문자 찾기

문자열.capitalize() : 첫문자 대문자

문자열.lower() : 소문자로 바꾸기

문자열.upper() : 대문자로 바꾸기



## 포매팅

"문자열 %s, %d, %c ,%.1f   " % 인덱스  : 문자열 뒤에 % 인덱스 를 통행 인덱스에 있는 값 출력

print("내용", end=" " ) 내용 끝나고 끝에 end 에 있는 것을 붙임.



- 가장 쓰기 편한 포맷팅

``` python
print(f"{a}번째로 들어온것은 {b}입니다.{1000:,.1f}원을 얻었습니다,")
```

``` python
a=1
print(f"3자리를 유지하고 앞에 0을 채우려면 {a:03d}를 쓰면 된다.")
```



변수형태 확인 : type()

상수 변환값 : int(), str(), float() 서로 변환 가능

배열 변환값 : str(), list(), tuple(), set()

-  str은 배열로도 숫자로도 형변환 할 수 있다는 것을 알아두자.





## sort

 `sorted_list=sorted(a,key=lambda x: (x[1],x[2],x[0]), reverse=True)`

key에 다음과 같이 함수 삽입 가능 이럴경우 x[1]을 우선으로 정렬 , `key=len`의 경우 길이를 대상으로 정렬 

리스트.sort(reverse=True) : 요소 정렬 reverse=True면 내림차순

- 리스트.sort() 시 본체 정렬
- sorted(리스트) 시 새로운 정렬 리스트 반환 / 본래 리스트는 유지





## 사용자가 입력한 값 받기

input("출력 메세지 : ")  입력한 값을 str 형태로 받음. 

숫자를 입력받고 싶으면 다음과 같이 사용

`int(input("숫자를 입력하세요 :"))`





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

리스트.index(요소) : 해당 요소의 인덱스 값 반환  / 찾을 문자가 없으면 에러 / 문자열,리스트, 튜플

문자열.find(요소) : 해당 요소의 인덱스 값 반환  / 찾을 문자가 없으면 -1 / 문자열만 사용

리스트[인덱스] : 해당 인덱스의 요소 값 반환

list(map(int,리스트)) : 리스트 내부 요소 int로 변환

sum(리스트) : 리스트 요소들의 합



- 만약 list1 형태가 [(1,2,3), ("a","b","c")] 형태라면 `for x,y,z in list1` 형태로 사용가능.



import collections

collections.Counter(리스트) : 리스트 내부 요소들의 갯수 세기



[ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]

 [y for x, y in zip([1,2,3], [3,2,1])]





## 집합

set1.remove()

set1.pop()

set1&set2 : 교집합(intersection)

set1|set2 : 합집합(union)

set1-set2 : 차집합(difference)

set1^set2 : 합집합-교집합 (symmetric_difference)





## 딕셔너리

dict1["key1"] : value1 출력

dict1["key1"]=value1 : {key1, value1} 쌍 대입, 수정

list(dict1.keys()) : 키값을 리스트로 출력 ( =list(dict)와 동일값)

list(dict1.values()) : 값을 리스트로 출력

list(dict1.items()) :  [(key1,value1), (key2,value2)] 형태로 반환

[(key1,value1), (key2,value2)]의 형태에서 dict 사용시 쉽게 dict 형태로 변환

list1=[key1,key2], list2=[value1,value2] 의 형태에서는 dict(zip(list1,list2)) 형태를 쓸 것



## break, continue

break : 반복문 자체를 빠져나옴.

continue : 이번회차 반복을 중단함.



## list comprehension

[표현식 for 변수 in 리스트  객체 if 조건식]

`[ i*2 for i in list1 if i%2==0]`



## 자주 사용되는 표준 라이브러리

- math,
- itertools : 
  - permutations(리스트, 개수)  : 개수를 뽑는 모든 순열 구하기(순서고려 o)
  - combinations(리스트, 개수)  : 개수를 뽑는 모든 조합 구하기(순서고려 x)
  - products(리스트, 개수) : 개수를 뽑는 모든 순열(중복허용)
  - combinations_with_replacement(리스트, 개수) : 개수를 뽑는 모든 조합(중복허용)
- heapq : 정렬 및 최대최소 최적화
  - eapq.heappush(리스트, 요소) : 리스트에서 요소 삽입
  - heapq.heappop(리스트, 요소) : 리스트에서 요소 꺼내기
- bisect
- collections
- random



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



## OS 모듈

`os.listdir()` : 파일 내부에 있는 파일을 모두 불러옴.

`os.getcwd()` : 현재 경로 출력

`os.mkdir()` : 경로에 폴더 생성

`os.path.join('-','test') ` : 현재 os의 파일 구분자로 연결

`os.path.abspath('파일명')` :지정된 파일의 절대 경로 반환

`os.path.isfile()` : 파일이 있는지 확인

`os.path.isdir()` : 폴더가 있는지 확인

`os.path.split()` : 폴더를 디렉토리명과 파일명으로 나눔

`os.path.splitext()` : 파일명과 확장자를 나눔

 



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
with open('07-07\\hello.txt','r') as pr: #해당폴더에서 07-07 폴더 열고 거기서 hello.txt 파일 열기
    for line in pr:
        print(line)
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

# with문은 open과 close를 같이 처리. 닫는 작업을 없앰.
```





## Class

```python
class Calculator:		#calculator 객체 생성
    def __init__(self):		# 초기값 지정
        self.result = 0

    def add(self, num):		#
        self.result += num
        return self.result

cal1 = Calculator() # cal1 객체 생성하기  cal1은 Calculator의 객체
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
```





##  객체와 인스턴스

클래스로 만든 객체를 인스턴스라고도 한다. 

a = Cookie() 이렇게 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 

즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. 



## 메서드 사용

``` python
a=Class()
Class.method(self, int a, int b)

a.method(int a, int b)
```

위형태로 클래스를 쓸 때는 self 사용 가능, 밑의 방식에서는 self는 반드시 생략



## `__init__`

`__init__` 이 있을 때는 초기값을 설정해줘야 class 가 생성됨

```python
a=FourCal(4,3)
```



## 상속

``` python
class MoreFourCal(FourCal): # 자식 클래스(부모클래스)
    def method2():
        pass
```



## 모듈

.py 파일 단위로 함수, 변수, 클래스의 모음이다.

`import 모듈명` 혹은 `from 모듈명 import 함수명 ` 으로 사용가능

앞의 모듈을 가져온 경우 모듈명.함수명으로 씀.

뒤의 함수를 가져온 경우 함수명으로 바로 사용 가능.

모듈 실행을 위해서는 같은 폴더에 존재해야함.



## `__name__`

`C:\doit>python mod1.py`처럼 

직접 mod1.py 파일을 실행할 경우 mod1.py의 `__name__` 변수에는 `__main__` 값이 저장된다. 

하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 `__name__` 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

| 직접 실행  | import |
| ---------- | ------ |
| `__main__` | 모듈명 |





## 패키지

``` python
game/				#  game 패키지 안에
    __init__.py
    sound/			# sound 패키지 안에
        __init__.py
        echo.py		## echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```



* `__init__.py` 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 `__init__.py` 파일이 없다면 패키지로 인식되지 않는다.

  > ※ python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식한다([PEP 420](https://www.python.org/dev/peps/pep-0420/)). 하지만 하위 버전 호환을 위해 `__init__.py` 파일을 생성하는 것이 안전한 방법이다.





## try-except

``` python
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
```



## enumerate

``` python
for i, name in enumerate(['body', 'foo', 'bar']):
	print(i, name)

# 결과 index와 값을 동시에 출력
0 body
1 foo
2 bar
```



## eval

문자열을 실행한 결과를 반환해주는 함수

``` python
eval('divmod(4, 3)')
# 결과 (1,)1
```





## filter

``` python
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
# 결과 [1,2,6]
```



## instance

``` python
a=Person()
isinstance(a, Person)
# 결과 True
```



## map

``` python
def two_times(x): 
    return x*2

list(map(two_times, [1, 2, 3, 4]))
#결과 2,4,6,8

```



## 라이브러리

- [sys](https://wikidocs.net/33#sys)
- [pickle](https://wikidocs.net/33#pickle)
- [os](https://wikidocs.net/33#os)
- [shutil](https://wikidocs.net/33#shutil)
- [glob](https://wikidocs.net/33#glob)
- [tempfile](https://wikidocs.net/33#tempfile)
- [time](https://wikidocs.net/33#time)
- [calendar](https://wikidocs.net/33#calendar)
- [random](https://wikidocs.net/33#random)
- [webbrowser](https://wikidocs.net/33#webbrowser)



