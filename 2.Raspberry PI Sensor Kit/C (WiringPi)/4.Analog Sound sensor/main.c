/*
* 라즈베리파이 센서 키트 Analog Sound sensor 동작 예제
*
* 본 예제는 사운드 센서로 소리가 감지되면 LED를 깜빡여 주는 동작을 합니다. (0.5초 켜진 뒤 0.2초 꺼짐)
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), 아날로그 사운드 센서
* LED     : GPIO 38번 | BCM : 20 | wiringPi : 28 
* 아날로그 사운드 센서
* VCC 핀  : 3.3V | GND 핀 : GND
* DOUT    : GPIO 40번 | BCM : 21 | wiringPi : 29
*
* ※ 모듈 연결 시 극성에 주의해 주도록 합니다.
* 라즈베리파이는 아날로그 신호(AOUT) 수신이 되지 않기 때문에 디지털 핀(DOUT)만 사용합니다. 
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED  28 // LED wiringPi 번호 정의
#define DOUT 29 // Sound 센서 DOUT 핀 wiringPi 핀 번호 정의


int main (void){

    if (wiringPiSetup() == -1){
        return 1;
    }

    pinMode(LED, OUTPUT);     // LED 제어 핀을 출력으로 설정
    pinMode(DOUT, INPUT);     // Sound 센서 디지털 데이터 수신 핀을 입력으로 설정

    digitalWrite(LED, 0);     // LED 초기값 Off

    while(1){

        if(digitalRead(DOUT) == 0){   // Sound 센서로부터 신호가 수신되면 (대기 HIGH, 소리 인식시 LOW)
    
            digitalWrite(LED, 1);       // LED On
            delay(500);                 // 500mS 지연

            digitalWrite(LED, 0);       // LED Off
            delay(200);                 // 200mS 지연
        }
    }

    return 0;
}