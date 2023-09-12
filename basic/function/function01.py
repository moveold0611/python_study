# def(define) -> 함수를 정의한다.

# 오버로딩 불가
def add(x, y):
    result = x + y
    return result
    
def add(*a): # 변수 여러개 사용
    print(type(a)) # 튜플 자료형으로 정의됨
    return a, 10 # 튜플로 묶어서 리턴됨

r = list(add(20, 10, 5, 30)) # 튜플을 리스트로 변환

print(r)



# kwarg

def sub(**data): # **이면 딕셔너리 자료형으로 매개변수 변환
    print(type(data))
    print(data)

sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)

sub({'a':1, 'b':2})
print()

# 초기값
def connection(password, serverName, ip='127.0.0.1', port='8080', username='root'): # 값을 넣지 않을 시 설정된 기본값을 사용
    print(f'ip: {ip}')
    print(f'port: {port}')
    print(f'serverName: {serverName}')
    print(f'username: {username}')
    print(f'password: {password}')

connection(serverName='test_server', password='1q2w3e4r', port='3306')

a = 2
def multi(a):
    return a ** 2

a = multi(a)
print(a)

def div():
    global a # 전역
    a = a * 10

div()
print(a)

def add(a, b):
    return  a + b

print(add(10, 20))

add = lambda a, b: a + b # lambda 매개변수 : 리턴
# 파이썬에서는 람다가 하나의 명령만 수행할 수 있다.