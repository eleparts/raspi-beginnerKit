'''
* 라즈베리파이 센서 키트 Passive Infrared sensor (PIR sensor) 동작 예제
*
* 본 예제는 PIR 센서로 물체가 감지되면 LED를 켜고, 시간이 지나 PIR 센서의 감지가 중단되면 LED를 꺼 주는 동작을 합니다.
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), PIR 센서 
* LED     : GPIO 38번 | BCM : 20
* PIR 센서 
* VCC 핀 : 5V | GND 핀 : GND
* OUT :  GPIO 40번 | BCM : 21 | wiringPi : 29
*
* ※ 모듈 및 LED 연결 시 극성에 주의해 주도록 합니다.
* PIR 센서는 물체의 움직임이 감지되면 일정 시간동안 OUT 포트로 HIGH 시간을 출력합니다. 
* 감도 및 HIGH 신호 출력 시간은 센서 본체의 가변저항으로 조절할 수 있습니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
'''

import RPi.GPIO as GPIO
import time

LED = 20 # LED BCM 핀 번호 정의
PIR = 21 # PIR 센서 BCM 핀 번호 정의

# GPIO.setwarnings (False)  #GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      #BCM 핀 번호 사용

GPIO.setup(LED, GPIO.OUT)   # LED 제어 핀을 출력으로 설정
GPIO.setup(PIR, GPIO.IN)    # PIR 센서 데이터 수신 핀을 입력으로 설정

GPIO.output(LED, False)     # LED 초기값 Off


try:

    while 1:

        if (GPIO.input(PIR)):       # PIR 센서로부터 HIGH 신호가 수신되면

            GPIO.output(LED, True)    # LED On
            time.sleep(0.2)           # 0.2초 지연
        else:

            GPIO.output(LED, False)   # LED Off
            time.sleep(0.2)           # 0.2초 지연

finally:
        GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
        


