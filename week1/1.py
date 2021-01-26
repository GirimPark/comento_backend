# 2장

#   정수형
import sys
from copy import copy
a = 123
a = -178
a = 0

#   실수형
a = 1.2
a = -3.45
a = 4.24E10
a = 4.24e-10

#   8진수와 16진수
a = 0o177
a = 0x8ff
b = 0xABC

#   연산자
a = 3
b = 4
print(a+b)
print(a*b)
print(a/b)
print(a**b)
print(7 % 3)
print(3 % 7)
print(7//4)


#   문자열
food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)
food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says."
print(say)

multiline = '''
Life is too short
You need python
'''
print(multiline)

head = "Python"
tail = " is fun!"
print(head + tail)
a = "python"
print(a*2)
print("="*50)
print("My Program")
print("="*50)

a = "Life is too short"
print(len(a))
print(a[3])
print(a[-1])
print(a[0:4])

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year, day, weather, ' ')

print("I eat %d apples" % 3)
print("I eat %s apples" % "five")
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))
print("I have %s apples" % 3)
print("Error is %d%%" % 98)

print("%10s" % "hi")
print("%-10sjane." % "hi")
print("%0.4f" % 3.421234234)
print("%10.4f" % 4.41234234)

print("I eat {0} apples".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(
    number=10, day=3))

print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

y = 3.421234234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

print("{{ and }}".format())

name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print(f"나는 내년이면 {age+1}살이 된다.")

d = {"name": '홍길동', 'age': 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f"{'hi':>10}")
print(f"{'hi':^10}")

a = "hobby"
print(a.count('b'))
print(a.find('k'))
# a.index('k') - 오류 발생

print(",".join('abcd'))
print("/".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = "   hi"
print(a.lstrip())
a = "hi   "
print(a.rstrip())
a = "   hi   "
print(a.strip())
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
b = "a:b:c:d"
print(b.split(':'))


#   리스트
a = [1, 2, 3]
print(a[0]+a[2])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[-1][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)

print(a)
a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a.reverse()
print(a)
print(a.index(3))

a = [1, 2, 3]
a.insert(0, 4)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a = [1, 2, 3]
a.extend([4, 5])
print(a)


#   튜플

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
'''
오류 발생
t1 = (1,2,'a','b')
del t1[0]
t1[0] = 'c'
'''
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[1:])

t2 = (3, 4)
print(t1+t2)
print(t2*3)
print(len(t1))


#   딕셔너리
dic = {'name': 'pey', "phone": "0119993323", 'birth': '1118'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}

a = {1: 'a'}
a[2] = 'b'
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])

a = {1: 'a', 1: 'b'}
print(a)

#   딕셔너리, 리스트는 변경 가능하므로 키 값에 올 수 없다.
#   a={[1,2]: 'hi'}

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())  # 리스트로 반환하지 않음

for k in a.keys():  # dict_keys로도 반복구문에 사용할 수 있음
    print(k)

list(a.keys())

a.values()

a.items()

a.clear()

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey'))  # 인덱스로 접근할 경우 오류 발생
print(a.get('foo', 'bar'))  # None대신 default값 반환

print('name' in a)
print('email' in a)


#   집합 자료형

s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))

s1 = set([1, 2, 3])
s1.add(4)
print(s1)
s1.update([4, 5, 6])
print(s1)
s1.remove(2)
print(s1)


#   bool
a = True
b = False
print(type(a))
print(type(b))

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

print(bool('python'))
print(bool(''))


#   변수
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
print(a is b)

b = copy(a)
print(b is a)

(a, b) = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a, b)

#   2장 연습문제
#   Q1
hong = [80, 75, 55]

print((hong[0]+hong[1]+hong[2])/len(hong))

#   Q2
num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

#   Q3
id = '881120-1068234'
print(id[:6])
print(id[7:])

#   Q4
pin = '881120-1068234'
print(pin[7])

#   Q5
a = "a:b:c:d"
a = a.replace(':', '#')
print(a)

#   Q6
l1 = [1, 3, 5, 4, 2]
l1.sort()
l1.reverse()
print(l1)

#   Q7
l2 = ['Life', 'is', 'too', 'short']
print((' '.join(l2)).lstrip())

#   Q8
t1 = (1, 2, 3)
print(t1+(4, ))  # 하나짜리 튜플은 (4, )와 같이 만들어야 함

#   Q9
#   3번: 키 값에 변경 가능한 리스트가 올 수 없다

#   Q10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop('B'))

#   Q11
a = [2, 2, 2, 1, 1, 3, 3, 3, 4, 4, 5]
print(set(a))

#   Q12
#   b의 값도 [1,4,3]으로 변경된다. a=b로 변수 a와 b가 가리키는 주소는 같기 때문이다


# 3장

#   if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

1 in [1, 2, 3]
1 not in [1, 2, 3]

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

score = 60
message = "success" if score >= 60 else "failure"

#   while문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee -= 1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다" % (money-300))
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

#   for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

add = 0
for i in range(1, 11):
    add += i
print(add)

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num*3 for num in a]
print(result)

result = [num*3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)

#   3장 연습문제
#   Q1
#   : shirt

#   Q2
num = 1
sum = 0
while num <= 1000:
    if num % 3 == 0:
        sum += num
    num += 1
print(sum)

#   Q3
num = 1
while num != 6:
    print('*' * num)
    num += 1

#   Q4
i = 1
for i in range(1, 101):
    print(i)

#   Q5
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in score:
    sum += i
print(sum/len(score))

#   Q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)


#   4장
#   함수
def add(a, b):
    return a+b


a = 3
b = 4
c = add(a, b)
print(a)


def say():
    return "Hi"


print(say())


def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


add(3, 4)


def say():
    print("Hi")


say()


def add(a, b):
    return a+b


result = add(a=3, b=7)
print(result)
result = add(b=5, a=3)
print(result)


def add_many(*args):  # *를 붙이면 입력값을 튜플로 만들어준다
    result = 0
    for i in args:
        result += i
    return result


def add_mul(choice, *args):
    result = 0
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


def print_kwargs(**kwargs):  # **를 붙이면 입력값들을 딕셔너리로 만듦
    print(kwargs)


print_kwargs(name='foo', age=3)


def add_and_mul(a, b):
    return a+b, a*b


print(add_and_mul(3, 4))


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")


say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

#   오류 발생
# def say_myself(name, man=True, old):
#     print("나의 이름은 %s 입니다."%name)
#     print("나이는 %d살입니다."%old)
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다")

a = 1


def vartest(a):
    a += 1


vartest(a)
print(a)

a = 1


def vartest(a):
    a = a+1
    return a


a = vartest(a)
print(a)

a = 1


def vartest():
    global a
    a = a+1


def add(a, b): return a+b


result = add(3, 4)
print(result)


#   사용자 입출력
# number = input("숫자를 입력하세요: ")
# print(number)

print("life" "is" "too short")
print("life"+"is"+"too short")
print("life", "is", "too shrot")
for i in range(10):
    print(i, end=' ')


#   파일 읽고 쓰기
f = open("새파일.txt", 'w')
f.close()

f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open("새파일.txt", 'r')
lines = f.readlines()  # lines는 리스트형
for line in lines:
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")


args = sys.argv[1:]
for i in args:
    print(i)

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=" ")

#   4장 연습문제
#   Q1


def is_odd(num):
    if(num % 2 == 0):
        return "짝수"
    else:
        return "홀수"


def is_odd(x): return "짝수" if x % 2 == 0 else "홀수"


#   Q2


def mean(*args):
    sum = 0
    for i in args:
        sum += i
    return sum/len(args)


#   Q3
# input1 = int(input("첫번째 숫자를 입력하세요: "))
# input2 = int(input("두번째 숫자를 입력하세요: "))

# total = input1+input2
# print("두 수의 합은 %s 입니다" % total)

#   Q4
#   3번: you need python

#   Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#   Q6
# with open("test.txt", 'a') as f:
#     input = input("내용을 입력하세요: ")
#     f.write(input)

#   Q7
with open("test.txt", 'w') as f:
    data = """Life is too short
you need java"""
    f.write(data)

with open("test.txt", 'r') as f:
    data = f.read()

data = data.replace("java", "python")

with open("test.txt", 'w') as f:
    f.write(data)


# 5장
#   클래스
result = 0


def add(num):
    global result
    result += num
    return result


print(add(3))
print(add(4))
#
result1 = 0
result2 = 0


def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
#


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
#


class FourCal:
    def __init__(self, first, second):  # 파이썬 생성자는 __init__
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
        #   파이썬 메서드의 첫 번재 매개변수는 관례적으로 self를 사용한다. self == 클래스의 인스턴스

    def add(self):
        result = self.first+self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def div(self):
        result = self.first/self.second
        return result


# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 8)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

a = FourCal(4, 2)
print(a.first)
#


class MoreFourCal(FourCal):  # 상속
    def pow(self):
        result = self.first**self.second
        return result


a = MoreFourCal(4, 2)
print(a.first)
print(a.add())
print(a.pow())
#


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second


a = SafeFourCal(4, 0)
print(a.div())
#


class Family:
    lastname = '김'


print(Family.lastname)

a = Family()
print(a.lastname)

Family.lastname = '박'
print(a.lastname)

#   모듈: 1_module.py

#   패키지: game

# game/sound/echo.py/echo_test()에서
# from으로 경로 접근 후에 echo_test()사용은 가능.
# 1. import game까지 하고 echo_test()로 접근하는 경우: game디렉터리의 모듈, game디렉터리의 __init__.py에 정의한 것만 사용 가능
# 2. import로 echo_test()까지 접근하는 경우: from없이 import만 사용할 때에는 마지막이 모듈/패키지여야 함

# __init__.py는 디렉터리가 패키지의 일부임을 알려준다.
# from game.sound import *: 해당 디렉터리 __init__.py에 __all__변수를 정의(마지막 항목이 패키지인 경우 해당)


#   예외 처리

try:
    4/0
except ZeroDivisionError as e:
    print(e)
#
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
#
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
#


class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
#


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
