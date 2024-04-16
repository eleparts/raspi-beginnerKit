'''
* 라즈베리파이 센서 키트 Temp & Humidity sensor 동작 예제 / Raspberry PI 5용 예제
*
* 본 예제는 온습도 센서에서 수신된 데이터를 터미널 창으로 반복해 출력하는 동작을 합니다.
* 
* 사용 소자 : 온습도 센서 
* 온습도 센서 
* VCC 핀 : 3.3V | GND 핀 : GND
* OUT :  GPIO 40번 | BCM : 21
*
* ※ 모듈 연결 시 극성에 주의해 주도록 합니다.
*
* 예제 실행 전 /boot/firmware/config.txt 경로에 dtoverlay=dht11,gpiopin=21 를 추가 후 재부팅해 줍니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
*
* 예제 정보 - 라즈베리파이 포럼 / danjperron
* https://forums.raspberrypi.com/viewtopic.php?t=366269
'''

import time

device0 = "/sys/bus/iio/devices/iio:device0"

#function to read first line and return integer

def readFirstLine(filename):
    try:
        f = open(filename,"rt")
        value =  int(f.readline())
        f.close()
        return True, value
    except ValueError:
        f.close()
        return False,-1
    except OSError:
        return False,0


try:
    while True:
        Flag, Temperature = readFirstLine(device0+"/in_temp_input")
        print("Temperature:",end="")
        if Flag:
            print(Temperature // 1000,"\u2103",end="\t")
        else:
            print("N.A.",end="\t")

        Flag, Humidity = readFirstLine(device0+"/in_humidityrelative_input")
        print("Humidity:",end="")
        if Flag:
            print(Humidity // 1000,"%")
        else:
            print("N.A.")
        time.sleep(2.0)
except KeyboardInterrupt:
    pass