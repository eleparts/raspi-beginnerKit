'''
* 라즈베리파이 센서 키트 Capacitive Touch sensor 동작 예제
*
* 본 예제는 터치센서에 접촉이 감지되면 LED를 켜 주고, 감지되지 않으면 LED를 꺼 줍니다.
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), 디지털 접촉식 터치센서 (정전식)
* LED     : GPIO 38번 | BCM : 20
* 디지털 접촉식 터치센서 (정전식)
* VCC 핀  : 3.3V | GND 핀 : GND
* DOUT    : GPIO 40번 | BCM : 21
*
* ※ 모듈 연결 시 극성에 주의해 주도록 합니다.
* 모듈 연결 시 전용 커넥터 케이블 연결 후 M/F 케이블을 이용해 라즈베리파이에 꽂아 주면 편리합니다.
* 라즈베리파이의 GND 핀은 여러개가 있으니 브레드보드를 통해 GND핀을 연결하지 않고 직접(ex 39번 핀) 꽂아 주어도 됩니다.
* 터치센서 보드에도 감지 LED가 있으며, 만약 터치 동작이 잘 안 되는 경우 터치 모듈의 연결 커넥터를 뽑았다가 다시 꽂아주시면 정상 동작됩니다. (기준 감지값 초기화)
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
'''

import RPi.GPIO as GPIO
import time

LED   = 20      # LED BCM 핀 번호 정의
DOUT  = 21      # 터치 센서 BCM 핀 번호 정의

# GPIO.setwarnings (False)  # GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setmode(GPIO.BCM)      # BCM 핀 번호 사용

GPIO.setup(LED, GPIO.OUT)   # LED 제어 핀을 출력으로 설정
GPIO.setup(DOUT, GPIO.IN)   # Sound 센서 데이터 수신 핀을 입력으로 설정

GPIO.output(LED, False)     # LED 초기값 Off

try:

  while 1:

    if (GPIO.input(DOUT)) :       # 터치 센서로부터 신호가 수신되면 (기본 LOW, 터치 인식시 HIGH)
      
      GPIO.output(LED, True)      # LED On
      
    else:
      GPIO.output(LED, False)     # LED Off

    time.sleep(0.2)               # 0.2초 지연
    
finally:
    GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 
    


