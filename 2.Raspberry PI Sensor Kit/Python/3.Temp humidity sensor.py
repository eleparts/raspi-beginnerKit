'''
* 라즈베리파이 센서 키트 Temp & humidity sensor 동작 예제
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
* 예제 실행 전 아래 명령어로 Adafruit_DHT 라이브러리를 설치해 주어야 합니다.
* sudo pip3 install Adafruit_DHT
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
*
# 원본 및 예제 라이브러리
# https://github.com/adafruit/Adafruit_Python_DHT
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
'''

import sys
import Adafruit_DHT

DHT11 = 11        # DHT22 = 11 | DHT22 = 22
DHT11_PIN = 21    # DHT11 BCM 핀 번호 정의 

try:

    while 1 :

        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(DHT11, DHT11_PIN)

        # Un-comment the line below to convert the temperature to Fahrenheit.
        # temperature = temperature * 9/5.0 + 32

        if humidity is not None and temperature is not None:
                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

        else:
                print('Failed to get reading. Try again!')
                # sys.exit(1)

finally:
        GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 



