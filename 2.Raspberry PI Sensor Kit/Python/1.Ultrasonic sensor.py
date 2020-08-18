'''
* 라즈베리파이 센서 키트 Ultrasonic sensor 동작 예제
*
* 본 예제는 Ultrasonic sensor(초음파 거리측정)의 예제로 초음파 센서와 물체의 거리를 터미널 창으로 실시간 출력해 줍니다.
* 
* 사용 소자 : Ultrasonic 센서
* VCC 핀  : 5V | GND 핀 : GND
* TRIG핀  : GPIO 38번 | BCM : 20
* ECHO핀  : GPIO 40번 | BCM : 21
*
* ※ 모듈 및 LED 연결 시 극성에 주의해 주도록 합니다.
* 초음파 센서는 센서에서 초음파를 방출, 다시 되돌아오는 시간을 측정합니다.
* 이를 이용해 앞에 있는 물체와의 거리를 계산, 측정할 수 있습니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
'''
import RPi.GPIO as GPIO
import time

TRIG = 20 # Trig 핀 BCM 번호 정의
ECHO = 21 # ECHO 핀 BCM 번호 정의

GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings (False)  #GPIO 사용중 경고 비활성화 명령, GPIO.cleanup() 사용 시 불필요

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try :

  while True :

    GPIO.output(TRIG, False)
    time.sleep(0.00001)

    GPIO.output(TRIG, True)                   # 10us 초음파 방사
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while(GPIO.input(ECHO) == 0):             # 초음파 송신 시간
      pulse_start = time.time()

    while(GPIO.input(ECHO) == 1):             # 초음파 수신 시간
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start  # 초음파 총 이동 시간 계산 

    distance = pulse_duration * (34000 / 2)   # 초음파 이동 시간으로 거리 계산 (공기 중 초음파 속도 약 340m/s, 이동거리/2)
    distance = round(distance, 1)

    print("Distance: ", distance, "cm")

    time.sleep(0.2)

finally:
    GPIO.cleanup()      # GPIO 상태 초기화, 없을 경우 예제 재 실행 시 사용중인 GPIO 경고 발생 