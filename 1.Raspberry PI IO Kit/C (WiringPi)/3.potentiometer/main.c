/*
* 라즈베리파이 입출력 키트 LED 구동 예제 02.ledsw
* 
* 사용 소자 : LED 1ea, 저항 1ea(220옴 권장), 가변저항
* LED : GPIO 16번 | BCM : 23 | wiringPi : 4
* 가변 저항 : GPIO 
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED 27           // BCM_GPIO 16 LED 정의
#define potentiometer /*GPIO 설정*/ // BCM_GPIO   LED 제어 가변저항 정의


int main (void){

  if (wiringPiSetup() == -1){
    return 1;
  }

  pinMode(LED, OUTPUT); // LED 출력핀으로 설정


  pinMode(potentiometer, INPUT);   // 가변 저항 입력핀으로 설정


  digitalWrite(LED, 0); // LED 초기값 Off


  while(1){

    if(digitalRead(SW_Y)){  // 가변저항으로 입력되는 값이 HIGH인 경우
  
      digitalWrite(LED, 1); // 노랑색 LED On
      delay(500); // 500ms(0.5초) 지연

    }else{                  // 가변저항으로 입력되는 값이 LOW인 경우

      digitalWrite(LED, 0); // 노랑색 LED Off
      delay(500); // 500ms(0.5초) 지연
    }
  }
  return 0;
}