import time

duration=int(input("Geri sayım için saniye giriniz: "))

while duration>0:
    print(duration)
    duration-=1
    time.sleep(1)
