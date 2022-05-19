# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이선의 선(철학)
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding) # 입력
print(sys.stdout.encoding) # 출력

# 출력문
print('My name is Goodboy! ')

# 변수 선언
myName = 'Badboy'

# 조건문
if myName == "Goodboy":
    print('Ok') # indent
    
# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)
        
# 함수 선언
def 인사():
    print("안녕. 하이.")
    
인사()

def greeting():
    print('Hello')
    
greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))