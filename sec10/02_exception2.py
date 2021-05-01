#예외처리

try:
    # print(10/0)
     print("나이"+23+"살")
except:
    print("오류발생")

try:
    print(10 / 0)
except Exception:    #범위가 너무 넓다는 경고
    print("오류발생")

