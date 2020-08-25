/*
* 라즈베리파이 입출력 키트 LED 구동 예제 04.ledpwm
* 
* 본 예제는 LED 1개를 반복해서 ON/OFF 해 줍니다.
* 이때, PWM을 이용하여 밝기가 조절됩니다.
*
* 사용 소자 : LED 1ea, 저항 1ea(220옴 권장)
* LED 1 : GPIO 16번 | BCM : 23 | wiringPi : 4
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
*/

#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h> 

#define LED 29 // LED wiringPi 핀 번호 정의 // 4 / 29


int main (void){

  if(wiringPiSetup() == -1){
    return 1;
  }

  pinMode (LED, OUTPUT);      
  softPwmCreate(LED, 0, 100);

  while(1){

    for(int i = 0; i<100; i=i+5){
      
      softPwmWrite(LED,i);
      delay(100);
    }

    for(int i = 100; i>0; i=i-5){
      
      softPwmWrite(LED,i);
      delay(100);
    }
  }
  return 0;
}