/*
* 라즈베리파이 센서 키트 Passive Infrared Sensor (PIR sensor) 동작 예제
*
* 본 예제는 PIR 센서로 물체가 감지되면 LED를 켜고, 시간이 지나 PIR 센서의 감지가 중단되면 LED를 꺼 주는 동작을 합니다.
* 
* 사용 소자 : LED 1ea, 저항 1ea (220옴), PIR 센서 
* LED : GPIO 38번 | BCM : 20 | wiringPi : 28 
* PIR 센서 
* VCC 핀 : 5V | GND 핀 : GND
* OUT :  GPIO 40번 | BCM : 21 | wiringPi : 29
*
* ※ 모듈 및 LED 연결 시 극성에 주의해 주도록 합니다.
* PIR 센서는 물체의 움직임이 감지되면 일정 시간동안 OUT 포트로 HIGH 시간을 출력합니다. 
* 감도 및 HIGH 신호 출력 시간은 센서 본체의 가변저항으로 조절할 수 있습니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWR8
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED 28 // LED wiringPi 번호 정의
#define PIR 29 // PIR 모듈 wiringPi 번호 정의


int main (void){

  if (wiringPiSetup() == -1){
    return 1;
  }

  pinMode(LED, OUTPUT);   // LED 제어 핀을 출력으로 설정
  pinMode(PIR, INPUT);    // PIR 센서 데이터 수신 핀을 입력으로 설정

  digitalWrite(LED, 0);   // LED 초기값 Off

  while(1){

    if(digitalRead(PIR)){     // PIR 센서로부터 HIGH 신호가 수신되면
  
      digitalWrite(LED, 1);   // LED On
      delay(200);             // 200mS 지연
    }else{

      digitalWrite(LED, 0);   // LED Off
      delay(200);             // 200mS 지연    
    }
  }

  return 0;
}