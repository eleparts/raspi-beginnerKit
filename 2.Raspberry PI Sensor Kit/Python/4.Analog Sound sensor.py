'''
* 라즈베리파이 센서 키트 Analog Sound sensor 동작 예제
*
* 본 예제는 사운드 센서로 소리가 감지되면 LED를 깜빡여 주는 동작을 합니다. (0.5초 켜진 뒤 0.2초 꺼짐)
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), 아날로그 사운드 센서
* LED     : GPIO 38번 | BCM : 20
* 아날로그 사운드 센서
* VCC 핀  : 3.3V | GND 핀 : GND
* DOUT    :  GPIO 40번 | BCM : 21
*
* ※ 모듈 연결 시 극성에 주의해 주도록 합니다.
* 라즈베리파이는 아날로그 신호(AOUT) 수신이 되지 않기 때문에 디지털 핀(DOUT)만 사용합니다. 
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
'''

import RPi.GPIO as GPIO
import time

LED   = 20  # LED BCM 핀 번호 정의
DOUT  = 21 # Sound 센서 DOUT 핀 BCM 핀 번호 정의

# GPIO.setwarnings (False)  #GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      #BCM 핀 번호 사용

GPIO.setup(LED, GPIO.OUT)   # LED 제어 핀을 출력으로 설정
GPIO.setup(DOUT, GPIO.IN)   # Sound 센서 데이터 수신 핀을 입력으로 설정

GPIO.output(LED, False)   # LED 초기값 Off

try:

  while 1:

    if (GPIO.input(DOUT) == 0) :  # Sound 센서로부터 신호가 수신되면 (기본 HIGH, 소리 인식시 LOW)

      GPIO.output(LED, True)      # LED On
      time.sleep(0.5)             # 0.5초 지연

      GPIO.output(LED, False)     # LED Off
      time.sleep(0.2)             # 0.2초 지연

finally:
    GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
    


