/*
* 라즈베리파이 입출력 키트 LED 구동 예제 01.led
* 
* 사용 소자 : LED 1ea, 저항 1ea(220옴 권장)
* LED 1 : GPIO 16번 | BCM : 23 | wiringPi : 4
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED1 4 // BCM_GPIO 23



int main (void){

  if(wiringPiSetup() == -1){
    return 1;
  }

  pinMode (LED1, OUTPUT);

  while(1){

    digitalWrite (LED1, 1); // LED ON
    delay (1000); // delay_1S

    digitalWrite (LED1, 0); // LED OFF
    delay (1000); // delay_1S

  }

  return 0;

}