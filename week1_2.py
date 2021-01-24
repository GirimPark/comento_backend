#   Q1
str = "a:b:c:d"
strList = str.split(':')
str = "#".join(strList)

print(str)


#   Q2
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

for i in A:
    if(i >= 50):
        sum += i

print(sum)


#   Q3
n = int(input())
Fibonacci = []

for i in range(n):
    if i > 1:
        Fibonacci.append(Fibonacci[i-2]+Fibonacci[i-1])
    elif i == 1:
        Fibonacci.append(1)
    else:
        Fibonacci.append(0)

print(Fibonacci)
