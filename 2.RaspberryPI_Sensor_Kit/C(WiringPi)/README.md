# RaspberryPI Sensor Kit  

[라즈베리파이 센서 키트](https://www.eleparts.co.kr/EPXDTWR8) 예제 코드 페이지입니다  

## C언어 사용을 위한 wirringPi 라이브러리 설치  

라즈베리파이 업데이트  

```bash
sudo apt-get update && sudo apt-get upgrade  
```

소스 관리 툴(git)다운로드 및 WiringPi 설치  

```bash
sudo apt-get install git-core  

git clone https://github.com/WiringPi/WiringPi  
cd WiringPi  
./build  
```

- 기존 제작자(Gordon)의 WiringPi가 공식적으로 지원을 중단함으로 인해 후속 WiringPi 작업 페이지를 사용합니다.  
[(Gordon's WiringPi 페이지 아카이브 - 지원 종료 안내)](https://web.archive.org/web/20220405225008/http://wiringpi.com/wiringpi-deprecated/)  
  
- 사용되는 후속 WiringPi 라이브러리 정보 : <https://github.com/WiringPi/WiringPi>  

- ※ (24년 04월) WiringPi는 PI5 지원을 위한 업데이트 중이지만, 일부 기능[(PWM등)](https://github.com/GrazerComputerClub/WiringPi/issues/21)에 제한이 있을 수 있습니다.  

GPIO 번호 확인

```bash
gpio readall  
```

> 위 명령어로 출력되는 GPIO 번호는 중앙의 Physical 번호(GPIO 번호) 및 BCM번호, wPi(wirringPi) 번호가 있습니다.  
> Physical 번호(GPIO 번호)는 실제 핀 배치 순서에 따라 부여한 번호이며, BCM 및 wPi 번호는 SW(소스코드)에서 사용하는 핀 번호입니다.  
>
> 본 예제 코드에서는 wPi(wirringPi)번호를 사용합니다.  
  
## C언어 예제 실행방법  

회로 연결은 **Schematics 디렉토리의 이미지 파일** 및 각 **예제 상단의 GPIO 안내**를 따라 해 주시면 됩니다.  

예제 실행은 각 예제 디렉토리로 이동해 아래 명령어로 컴파일&실행해 주시면 됩니다.  

```bash
gcc -o main main.c -lwiringPi

sudo ./main
```

예제 종료는 **`CTRL + C`** 키를 눌러 주시면 됩니다.  

## 예제 코드 간단 설명  

### 1.Ultrasonic_sensor  

초음파 센서 : 초음파를 발사, 정면에 있는 물체(장애물)과의 거리를 측정해 터미널로 출력해 줍니다.  

### 2.Passive_Infrared_sensor (PIR sensor)  

디지털 적외선 물체 감지 센서 : 센서 정면 일정 범위의 움직임을 감지하여 LED를 ON 해 줍니다.  

### 3.Temp_Humidity_sensor  

온습도 센서 : 온도&습도를 측정하여 터미널로 출력해 줍니다.  

### 4.Analog_Sound_sensor  

아날로그 사운드 센서 : 소리가 감지되면 잠시 LED를 켜 줍니다.  

### 5.Capacitive_Touch_sensor  

디지털 정전식 터치센서 : 터치가 감지되면 LED를 켜 줍니다.  
