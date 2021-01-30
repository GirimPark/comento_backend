#   내장 함수
print(abs(-3))

print(all([1, 2, 3, 0]))
print(all([]))

print(any([1, 2, 3, 0]))
print(any([0, ""]))
print(any([]))

print(chr(97))

print(dir([1, 2, 3]))
print(dir(dict))

print(divmod(7, 3))

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#   입력받은 문자열로 함수, 클래스를 동적으로 실행할 때 사용
print(eval('1+2'))
print(eval('"hi"+"a"'))
print(eval('divmod(4,3)'))
#


def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)

    return result


print(positive([1, -3, 2, 0, -5, 6]))

# -> #


def positive(x):
    return x > 0


print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# -> #
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))


print(hex(234))

a = b = 3
print(id(a))
print(id(b))
print(id(3))

# a=input()
# print(a)

print(int(3.4))
print(int('11', 2))
print(int('1A', 16))

#


class Person:
    pass


a = Person()
print(isinstance(a, Person))
#
len("python")
len([1, 2, 3])

print(list("python"))
a = [1, 2, 3]
b = a
print(b)
print(id(b))
b = list(a)
print(b)
print(id(b))

#


def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result


result = two_times([1, 2, 3, 4])
print(result)

# -> #


def two_times(x):
    return x*2


print(list(map(two_times, [1, 2, 3, 4])))
print(map(two_times, [1, 2, 3, 4]))  # 주소 반환

# -> #
print(list(map(lambda a: a*2, [1, 2, 3, 4])))

print(max([1, 2, 3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))

print(oct(34))
print(oct(12345))

f = open("binary_file", 'wb')
f.write(bytes(97))
f.write(bytes(98))
f.close()
f = open("binary_file", 'rb')
print(f.read(1))
f.close()

print(ord('a'))

print(pow(2, 4))

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))

print(round(4.6))

print(sorted([3, 1, 2]))
print([3, 1, 2].sort())  # 결과반환 x

print(str(3))

print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

print(tuple("apbc"))

print(type("ABC"))

print(list(zip([1, 2, 3], [4, 5, 6])))  # zip의 인수들은 동일한 개수로 이루어진 자료형
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))


#   라이브러리 > 1_3.py
