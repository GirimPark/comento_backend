#   라이브러리
import threading
import webbrowser
import random
import calendar
import time
import tempfile
import glob
import shutil
import os
import pickle
import sys

# import sys
print(sys.argv)
# sys.exit()
print(sys.path)

# import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)
f.close()

# import os
print(os.environ)
print(os.environ['PATH'])
# os.chdir("C:\BracketsSpace")
print(os.getcwd())
print(os.system("dir"))

f = os.popen("dir")
print(f.read())

# os.mkdir(디렉터리생성)
# os.rmdir(비어있는 디렉터리삭제)
# os.unlink(파일지우기)
# os.rename(바꿀이름, 바꾼이름)

# import shutil
shutil.copy("src.txt", "dst.txt")

# import glob
print(glob.glob("D:/Microsoft VS Code/bin/comento_backend/week1/1*"))

# import tempfile
filename = tempfile.mkstemp()
print(filename)
f = tempfile.TemporaryFile()
f.close()

# import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
# for i in range(10):
#     print(i)
#     time.sleep(1)

# import calendar
# print(calendar.calendar(2021)) == print(calendar.prcal(2021))
print(calendar.prmonth(2021, 1))
print(calendar.weekday(2021, 1, 28))
print(calendar.monthrange(2021, 1))

# imprt random
print(random.random())
print(random.randint(1, 10))


def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)
# def random_pop(data):
#     number=random.choice(data)
#     data.remove(number)
#     return number


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

# import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")


#   스레드

# 25초가 걸리는 프로세스
# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# for i in range(5):
#     long_task()

# print("End")

# -> #
# imprt threading


def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)


print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()    # 해당 스레드가 종료될 때까지 기다림

print("End")
