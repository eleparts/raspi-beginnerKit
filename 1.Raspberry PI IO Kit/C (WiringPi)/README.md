# Raspberry PI I/O Kit  

[라즈베리파이 입출력 키트](https://www.eleparts.co.kr/EPXDTWPM)  

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
>
> Physical 번호(GPIO 번호)는 실제 핀 배치 순서에 따라 부여한 번호이며, BCM 및 wPi 번호는 SW(소스코드)에서 사용하는 핀 번호입니다.  
>
>본 예제 코드에서는 wPi(wirringPi)번호를 사용합니다.  
  
## C언어 예제 실행방법  

회로 연결은 Schematics 디렉토리의 이미지 파일 및 각 예제 상단의 GPIO 안내를 따라 해 주시면 됩니다.  

예제 실행은 각 예제 디렉토리로 이동해 아래 명령어로 컴파일&실행해 주시면 됩니다.  

```bash
gcc -o main main.c -lwiringPi

sudo ./main
```

예제 종료는 **`CTRL + C`** 키를 눌러 주시면 됩니다.  

## 예제 코드 간단 설명  

### 1.led  

LED 1개의 ON/OFF 반복 동작을 합니다.  

### 2.led&sw  

LED 3개 및 SW(스위치) 3개를 이용해 각 스위치를 누르면 해당하는 LED가 0.5초간 켜집니다.  

### 3.potentiometer  

가변저항으로 변화하는 전압을 입력받아 LED를 ON/OFF 해 줍니다.  
※ 라즈베리파이의 GPIO에는 ADC가 없으며, ADC 기능을 사용하는것이 아닌 단순 디지털 입력 (H/L)으로 제어합니다. (상세 설명은 코드 참조)  
