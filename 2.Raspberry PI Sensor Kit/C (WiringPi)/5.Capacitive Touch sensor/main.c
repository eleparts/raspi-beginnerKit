/*
* 라즈베리파이 센서 키트 Capacitive Touch sensor 동작 예제
*
* 본 예제는 터치센서에 접촉이 감지되면 LED를 켜 주고, 감지되지 않으면 LED를 꺼 줍니다.
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), 디지털 접촉식 터치센서 (정전식)
* LED     : GPIO 38번 | BCM : 20 | wiringPi : 28 
* 디지털 접촉식 터치센서 (정전식)
* VCC 핀  : 3.3V | GND 핀 : GND
* DOUT    : GPIO 40번 | BCM : 21 | wiringPi : 29
*
* ※ 모듈 연결 시 극성에 주의해 주도록 합니다.
* 모듈 연결 시 전용 커넥터 케이블 연결 후 M/F 케이블을 이용해 라즈베리파이에 꽂아 주면 편리합니다.
* 라즈베리파이의 GND 핀은 여러개가 있으니 브레드보드를 통해 GND핀을 연결하지 않고 직접(ex 39번 핀) 꽂아 주어도 됩니다.
* 터치센서 보드에도 감지 LED가 있으며, 만약 터치 동작이 잘 안 되는 경우 터치 모듈의 연결 커넥터를 뽑았다가 다시 꽂아주시면 정상 동작됩니다. (기준 감지값 초기화)
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED  28 // LED wiringPi 번호 정의
#define DOUT 29 // 터치 센서 wiringPi 핀 번호 정의


int main (void){

  if (wiringPiSetup() == -1){
    return 1;
  }
  
  pinMode(LED, OUTPUT);   // LED 제어 핀을 출력으로 설정
  pinMode(DOUT, INPUT);   // 터치 센서 데이터 수신 핀을 입력으로 설정

  digitalWrite(LED, 0);   // LED 초기값 Off

  while(1){

    if(digitalRead(DOUT)){     // 터치 센서로부터 신호가 수신되면
      
      digitalWrite(LED, 1);    // LED On
      
    }else{
      
      digitalWrite(LED, 0);    // LED Off      
    }

    delay(200);                // 200mS 지연
  }
  return 0;
}