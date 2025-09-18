from time import sleep

for i in range(1, 11):
    sleep(1)
    if i == 6:
        break
    print(i)