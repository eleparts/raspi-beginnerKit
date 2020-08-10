/*
* 라즈베리파이 입출력 키트 LED 구동 예제 02.ledsw
* 
* 사용 소자 : LED 3ea, 스위치 3ea, 저항 3x2ea (220옴(led) 3ea, 10k옴(스위치) 3ea 권장)
* LED 1 : GPIO 36번 | BCM : 16 | wiringPi : 27 
* LED 2 : GPIO 38번 | BCM : 20 | wiringPi : 28 
* LED 3 : GPIO 40번 | BCM : 21 | wiringPi : 29 
* SW 1  : GPIO 29번 | BCM :  5 | wiringPi : 21 
* SW 1  : GPIO 31번 | BCM :  6 | wiringPi : 22 
* SW 1  : GPIO 33번 | BCM : 13 | wiringPi : 23 
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED_Y 27 // BCM_GPIO 16 노랑색 LED 정의
#define LED_R 28 // BCM_GPIO 20 빨간색 LED 정의
#define LED_G 29 // BCM_GPIO 21 초록색 LED 정의

#define SW_Y 21 // BCM_GPIO 5  노랑색 LED제어 스위치 정의
#define SW_R 22 // BCM_GPIO 6  빨간색 LED제어 스위치 정의
#define SW_G 23 // BCM_GPIO 13 초록색 LED제어 스위치 정의


int main (void){

  if (wiringPiSetup() == -1){
    return 1;
  }

  pinMode(LED_Y, OUTPUT); // 노랑색 LED 출력핀으로 설정
  pinMode(LED_R, OUTPUT); // 빨간색 LED 출력핀으로 설정
  pinMode(LED_G, OUTPUT); // 초록색 LED 출력핀으로 설정

  pinMode(SW_Y, INPUT);   // 노랑색 LED제어 스위치 입력핀으로 설정
  pinMode(SW_R, INPUT);   // 빨간색 LED제어 스위치 입력핀으로 설정
  pinMode(SW_G, INPUT);   // 초록색 LED제어 스위치 입력핀으로 설정


  while(1){

    digitalWrite(LED_Y, 0); // LED 초기값 Off
    digitalWrite(LED_R, 0); // LED 초기값 Off
    digitalWrite(LED_G, 0); // LED 초기값 Off

    if(digitalRead(SW_Y) == 0){  // 노랑색 LED제어 스위치가 눌리면
  
      digitalWrite(LED_Y, 1); // 노랑색 LED On
      delay(500); // mS
    }

    if(digitalRead(SW_R) == 0){  // 빨간색 LED제어 스위치가 눌리면

      digitalWrite(LED_R, 1); // 빨간색 LED On
      delay(500); // mS
     }

     if(digitalRead(SW_G) == 0){  // 초록색 LED제어 스위치가 눌리면

      digitalWrite(LED_G, 1); // 초록색 LED On
      delay(500); // mS
    }
  }

  return 0;
}