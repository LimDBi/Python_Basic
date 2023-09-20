# 문자열의 이해(String)

# 1. 문자열 인덱스
#  - 문자열은 각 문자마다 순서(인덱스)가 있음
#  - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#  - 인덱스 시작은 0
#  - 인덱스는 공백 포함
print("="*200)
print("Python")

# 2. 문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류(Error: string index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[19])

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1 (-0아님)
print(lang[-1]) # (출력: n)
print(lang[-3]) # (출력: h)

# ID를 Email: cherry1024@gmail.com
# - 로그인: cherry1024@gmail.com님 --> cherry1024님으로 출력 나중에..

# 3. 문자열 슬라이싱
# - lang[3]: 문자 1개만 추출
# - 부분 문자열을 추출하고 싶은 경우
# - 시작인덱스, 끝인덱스 필요
msg = "Python is all you need"
print(msg[0:6]) # 끝 인덱스는 +1 한 값으로 입력
print(msg[:6]) # 시작 인덱스 생략 시 자동으로 0 입력
print(msg[3:]) # 끝 인덱스 생략 시 자동으로 -1 입력
print(msg[:]) # 인덱스 전부 생략 시 자동으로 0, -1 입력

print("="*200)
print(msg[18:])
print(msg[-4:])

# 4. 문자열 함수
str = "Hello world"  #인덱스 0~10, -1~-11 정방향은 11부터 out of range, 역뱡향은 -12부터

print("="*200)
# 4-1. len() : 문자열 길이 계산
print(len(str))

# 4-2. upper() and lower() : 대소문자 변경
#  - 데이터 전처리: 1A, 1a => 1A 통일(upper() 사용해서)
print(str.upper())
print(str.lower())

# 4-3. replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4 split() : 구분자를 기준으로 분자열 분활(Defalut: 공백)
b = "hello world what a nice weather"
print(b.split("w"))
print(b.split())

# 4-5 strip() : 문자열의 좌우 공백을 제거
id = "                        python1004                       "
print(id)
print(id.strip())

# 4-6 find() and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력 *자기가 시작한 부분에서 처음 만난 문자만 찾음. 중복 고려 X*
print(str.find("o"))  #Hello의 o의 인덱스 4를 출력
print(str.rfind("o"))  #World의 o의 인덱스 7을 출력
print(str.find("world")) # 단어를 넣으면 단어의 첫 알파벳의 인덱스 6을 출력
print(str.find("World"))  #없으면 -1출력
print(str.rfind("world"))  #첫글자의 인덱스 출력
print(str.rfind("World"))  #rfind()도 없으면 -1 출력

# 4-7. in() : 특정 문자열 포함하는지 확인(True, False로 출력)
# print("Hi", in"Hi Python")  #True 출력.

# 1. id = "cherry1004@gmail.com"
# -> id만 추출 "cherry1004"
#    "job1234@gmail.com"
#    "abc@gmail.com"
id = "cherry1004@gmail.com"
print(id[0:id.find("@")])  #제일 심플한 방법
id1 = "job1234@gmail.com"
id2 = "abc@gmail.com"
val = id1.find("@")
print(id1[0:val])
val1 = id2.find("@")
print(id2[0:val1])

# naver, daum, google만 추출 코드
url = "www.naver.com"
print(url.split("."))
print(url.rfind("."))
print(url.find("."))
print(url[url.find(".") + 1 : url.rfind(".") ])
# 가독성이 좋은 코드
# start = url.find(".") +1
# end = url.rfind(".")
# val = url[start:end]
# print(val)
