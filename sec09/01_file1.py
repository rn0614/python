# 파일 입출력

# open(파일명, 열기모드) / -r -w -a

# close()

#파일 생성 : 파일 명만 적으면 현재 디렉토리에 생성

#f= open("file.txt", 'w')
#f.close()

# 실행시 run으로

# f = open("C:\\python\file2.txt", 'w')
# f.close()

data='안녕하세요'
f = open("file2.txt", 'w', encoding='utf-8')
f.write(data)
f.close()


f= open("file4.txt", 'w', encoding='utf-8')

for i in range(1,11):
    data


