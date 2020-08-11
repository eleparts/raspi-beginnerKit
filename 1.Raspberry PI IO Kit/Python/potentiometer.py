"""
* 라즈베리파이 입출력 키트 LED 구동 예제 02.ledsw
* 
* 사용 소자 : LED 1ea, 저항 1ea(220옴 권장), 가변저항
* LED      : GPIO 16번 | BCM : 23
* 가변 저항 : GPIO 18번 | BCM : 24
*
* 가변저항을 사용하는 경우 양 끝을 VCC(+)및 GND(-)에 연결하면 중앙 핀에서 아날로그 신호를 얻을 수 있습니다.
* 이 신호는 ADC 기능을 이용하면 ADC성능에 따라 매우 다양한(10bit ADC = 1024) 값을 얻을 수 있으나 라즈베리파이의 GPIO는 ADC 기능을 지원하지 않습니다.
* 라즈베리파이에서 ADC 기능을 이용하기 위해서는 별도의 ADC칩(모듈)을 사용해야 하며, 여기서는 GPIO의 디지털 입력 기능의 테스트 용도로만 사용합니다.
*
* 디지털 입력은 0V=LOW, 3.3V=HIGH 처럼 정확한 값으로 판단하지 않으며, 0V ~ 1V 범위는 LOW, 2V ~ 3.3V는 HIGH와 같이 일정 범위를 H/L로 판단합니다. 
* 이 경우 1~2V에서는 H/L가 정확하지 않은 상태가 되며, 이 전압 범위 내에서는 가변저항을 돌리지 않아도 High 혹은 Low가 고정되지 않고 변경되는 동작이 있을 수 있습니다.
* ※ 전압 값은 예시이며 정확한 정보는 칩셋 데이터시트 참고
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
"""

import RPi.GPIO as GPIO
import time

LED = 23           # LED BCM 핀 번호 정의
potentiometer = 24 # 가변저항 BCM 핀 번호 정의

# GPIO.setwarnings (False)  # GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      # BCM 핀 번호 사용

GPIO.setup(LED, GPIO.OUT)            # LED 출력핀으로 설정
GPIO.setup(potentiometer, GPIO.IN)   # 가변 저항 입력핀으로 설정
GPIO.output(LED, False)              # LED 초기값 Off

try:

  while 1:

    if (GPIO.input(potentiometer)):  # 가변저항으로 입력되는 값이 HIGH인 경우

      GPIO.output(LED, True)         # LED On
      time.sleep(0.2)                # 0.2초 지연

    else:                            # 가변저항으로 입력되는 값이 LOW인 경우

      GPIO.output(LED, False)        # LED Off
      time.sleep(0.2)                # 0.2초 지연

finally:
    GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
    