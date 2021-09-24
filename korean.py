import time

timer = int(input("타이머를 입력해주세요(초 단위) : "))

for i in range(timer):
    print(timer)
    timer -= 1
    time.sleep(1)
print("끝")

#한글