"""
* 라즈베리파이 입출력 키트 LED 구동 예제 01.led
* 
* 사용 소자 : LED 1ea, 저항 1ea(220옴 권장)
* LED 1 : GPIO 16번 | BCM : 23 
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
"""
import RPi.GPIO as GPIO
import time

LED = 23 # LED 핀 번호 정의 BCM 23 Pin | GPIO 16

# GPIO.setwarnings (False)  #GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      #BCM 핀 번호 사용
GPIO.setup(LED, GPIO.OUT)   #LED(BCM 23번 핀) OUT 로 설정


try:        

  while 1:

    GPIO.output(LED, True)   # LED ON
    time.sleep(1) # 1초 지연

    GPIO.output(LED, False)  # LED OFF
    time.sleep(1) # 1초 지연

finally:
    GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
    