# 변수와 할당 - 값에 이름 붙이기
# 형식: 변수이름 = 값 <-오른쪽 값을 왼쪽 이름에 "저장"하라는 뜻
temp = 25
name = "센서A"
COUNT = 3

print(temp) #25
print("temp")
x=10
x=x+5
print(x) #15
# 변수 이름 규칙
# 형식:영문자,숫자,밑줄 사용 가능 / 숫자로 시작 불가/ 공백 불가
sensor_count = 3  #snake_case
temp2 = 10        #숫자 사용 가능(숫자 시작x)

# 대소문자 구분, 재할당
temp=25
Temp=100
print(temp, Temp) #25 100
# 재할당 : 마지막 저장값만 남음
score=10
score=20
score=30
print(score) #30

temp = 25
print(temp) #25
name = "센서A"
print(name)
temperature = 30
print(temperature) #30
my_number = 7
print(my_number) #7
mood = "행복"
print(mood) #행복
age = 27
lable = "나이"
print(lable) #나이
print(age)  #27
x = 10
x = x+5 #15
print(x)
x = x*2 #30
print(x)
a = 100
b = a
a = 999
print(a,b) #999, 100

orange = 25
print(orange)
score = 90
print(score)

temp = 25 #온도(섭씨)
count = 3 #센서 개수
#temp = 100
print(temp)