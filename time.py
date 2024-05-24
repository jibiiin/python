import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
for a in range(0,10):
    print(a)
    time.sleep(2)