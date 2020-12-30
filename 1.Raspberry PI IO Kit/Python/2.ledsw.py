"""
* 라즈베리파이 입출력 키트 스위치 동작 예제 02.ledsw
*
* 본 예제는 3개의 스위치를 누르면 각각의 스위치에 해당하는 LED를 켜는 동작을 수행 합니다.
* 
* 사용 소자 : LED 3ea, 스위치 3ea, 저항 3x2ea (220옴(led) 3ea, 10k옴(스위치) 3ea 권장)
* LED 1 : GPIO 36번 | BCM : 16
* LED 2 : GPIO 38번 | BCM : 20
* LED 3 : GPIO 40번 | BCM : 21
* SW 1  : GPIO 29번 | BCM :  5
* SW 1  : GPIO 31번 | BCM :  6
* SW 1  : GPIO 33번 | BCM : 13
*
* 스위치를 연결할때는 VCC에 저항을 연결해 풀업 회로를 구성해 줍니다, 이때 VCC가 GND와 바로 연결되지 않도록(쇼트) 주의해야 합니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
"""

import RPi.GPIO as GPIO
import time

LED_Y = 16 # 노랑색 LED 정의 : BCM 16 PIN | GPIO 36
LED_R = 20 # 빨간색 LED 정의 : BCM 20 PIN | GPIO 38 
LED_G = 21 # 초록색 LED 정의 : BCM 21 PIN | GPIO 40

SW_Y =  5 # 노랑색 LED제어 스위치 정의 : BCM  5 PIN | GPIO 29
SW_R =  6 # 빨간색 LED제어 스위치 정의 : BCM  6 PIN | GPIO 31
SW_G = 13 # 초록색 LED제어 스위치 정의 : BCM 13 PIN | GPIO 33

# GPIO.setwarnings (False)  #GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      #BCM 핀 번호 사용

GPIO.setup(LED_Y, GPIO.OUT) # 노랑색 LED 출력핀으로 설정
GPIO.setup(LED_R, GPIO.OUT) # 빨간색 LED 출력핀으로 설정
GPIO.setup(LED_G, GPIO.OUT) # 초록색 LED 출력핀으로 설정

GPIO.setup(SW_Y, GPIO.IN)   # 노랑색 LED제어 스위치 입력핀으로 설정
GPIO.setup(SW_R, GPIO.IN)   # 빨간색 LED제어 스위치 입력핀으로 설정
GPIO.setup(SW_G, GPIO.IN)   # 초록색 LED제어 스위치 입력핀으로 설정

try:

    while 1:

        GPIO.output(LED_Y, False)   # LED 초기값 Off
        GPIO.output(LED_R, False) 
        GPIO.output(LED_G, False) 

        if (GPIO.input(SW_Y) == 0):   # 노랑색 LED제어 스위치가 눌리면

            GPIO.output(LED_Y, True)    # 노랑색 LED On
            time.sleep(0.5)             # 0.5초 지연

        if (GPIO.input(SW_R) == 0):   # 빨간색 LED제어 스위치가 눌리면

            GPIO.output(LED_R, True)    # 빨간색 LED On
            time.sleep(0.5)             # 0.5초 지연
        
        if (GPIO.input(SW_G) == 0):   # 초록색 LED제어 스위치가 눌리면

            GPIO.output(LED_G, True)    # 초록색 LED On
            time.sleep(0.5)             # 0.5초 지연

finally:
        GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
        