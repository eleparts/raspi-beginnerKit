# Raspberry PI I/O Kit  

[라즈베리파이 입출력 키트](https://www.eleparts.co.kr/EPXDTWPM) 예제 코드 페이지입니다  

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

- WiringPi가 공식적으로 지원을 중단함으로 인해 비공식 미러 페이지를 사용합니다.  [(관련 공지 URL)](http://wiringpi.com/wiringpi-deprecated/)  
  
GPIO 번호 확인

```bash
gpio readall  
```

> 위 명령어로 출력되는 GPIO 번호는 중앙의 Physical 번호(GPIO 번호) 및 BCM번호, wPi(wirringPi) 번호가 있습니다.  
> Physical 번호(GPIO 번호)는 실제 핀 배치 순서에 따라 부여한 번호이며, BCM 및 wPi 번호는 SW(소스코드)에서 사용하는 핀 번호입니다.  
>
>본 예제 코드에서는 wPi(wirringPi)번호를 사용합니다.  
  
## C언어 예제 실행방법  

회로 연결은 **Schematics 디렉토리의 이미지 파일** 및 각 **예제 상단의 GPIO 안내**를 따라 해 주시면 됩니다.  

예제 실행은 각 예제 디렉토리로 이동해 아래 명령어로 컴파일&실행해 주시면 됩니다.  

```bash
gcc -o main main.c -lwiringPi

sudo ./main
```

예제 종료는 **`CTRL + C`** 키를 눌러 주시면 됩니다.  
  
## Schematics  

Schematics 디렉토리에는 라즈베리파이의 **GPIO 번호 안내 사진(이미지)** 및 각 **예제별 배선 방법 사진(이미지)가** 안내되어 있습니다.  
GPIO 확장모듈을 사용하시는 경우 확장모듈을 브레드보드에 꽂고 점퍼를 확장 모듈이 연결된 브레드보드에 연결해 주시면 됩니다.  

## 예제 코드 간단 설명  

### 1.led  

LED 1개의 ON/OFF 반복 동작을 합니다.  

### 2.led&sw  

LED 3개 및 SW(스위치) 3개를 이용해 각 스위치를 누르면 해당하는 LED가 0.5초간 켜집니다.  

### 3.potentiometer  

가변저항으로 변화하는 전압을 입력받아 LED를 ON/OFF 해 줍니다.  
※ 라즈베리파이의 GPIO에는 ADC가 없으며, ADC 기능을 사용하는것이 아닌 단순 디지털 입력 (H/L)으로 제어합니다. (상세 설명은 해당 예제 코드 참조)  

### 4.ledpwm  
  
PWM 기능을 이용하며 LED의 밝기를 조절해 줍니다.  
PWM 기능은 LED를 매우 빠르게 깜빡이면서 각 깜빡임의 ON/OFF 비율을 조절하여 밝기를 조정합니다.  

### 5.adcspi  
  
ADC IC를 이용하면 라즈베리파이에서 지원하지 않는 ADC 기능을 이용해 아날로그 신호 데이터를 받아볼 수 있습니다.  
[MCP3204 ADC IC(별도 구매)](https://www.eleparts.co.kr/EPX3AHC4)를 이용하여 아날로그 데이터를 입력받고, SPI통신으로 라즈베리파이에 전달하여 출력해 줍니다.  
단, SPI 통신을 사용하기 위해서는 라즈베리파이 설정 창에서 **SPI 기능을 Enable** 해 주어야 합니다.  
  