# Raspberry PI I/O Kit  

[라즈베리파이 입출력 키트](https://www.eleparts.co.kr/EPXDTWPM) 예제 코드 페이지입니다  
  
## 라즈베리파이 5 사용 시 LGPIO 설치  
  
**라즈베리파이 5** 사용 시 아래 명령어로 **LGPIO**를 설치해 주어야 RPi.GPIO 라이브러리 사용이 가능합니다.  

```bash  
# 반드시 PI 5 사용시에만 설치
pip install --break-system-packages rpi-lgpio
```
  
Pi5가 아닌 경우 설치하면 분제가 생길 수 있습니다.  
  
## Python 예제 실행방법  

회로 연결은 **Schematics 디렉토리의 이미지 파일** 및 각 **예제 상단의 GPIO 안내**를 따라 해 주시면 됩니다.  

예제 실행은 각 예제를 `python` 로 실행해 주시면 됩니다.

```bash
python (예제 파일명).py
```

ex)  

```bash
python led.py
python ledsw.py
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
  