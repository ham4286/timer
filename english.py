import time

timer = int(input("timer(sec) : "))

for i in range(timer):
    print(timer)
    timer -= 1
    time.sleep(1)
print("END")

#english