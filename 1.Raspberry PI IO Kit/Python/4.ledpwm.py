"""
* 라즈베리파이 입출력 키트 LED 구동 예제 04.ledpwm
* 
* 본 예제는 LED 1개를 반복해서 ON/OFF 해 줍니다.
* 이때, PWM을 이용하여 밝기가 조절됩니다.
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

GPIO.setmode(GPIO.BCM)      # BCM 핀 번호 사용
GPIO.setup(LED, GPIO.OUT)   # LED(BCM 23번 핀) OUT 로 설정


pwm = GPIO.PWM(LED,50)      # 50hz, 1초에 50번 깜빡임
pwm.start(0)  

try:

    while 1:

        for duty in range(0,100,5):   # duty 를 0부터 100까지 증가

            pwm.ChangeDutyCycle(duty)   # duty 변경, 0-100 범위(%), 각 깜빡임 당 on/off 비율 조정
            time.sleep(0.1)

        for duty in range(100,0,-5):  # duty 를 100부터 0으로 감소

            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

finally:
    pwm.stop()
    GPIO.cleanup()
