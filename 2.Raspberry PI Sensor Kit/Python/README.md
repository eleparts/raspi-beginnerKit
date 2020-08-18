# Raspberry PI Sensor Kit  

[라즈베리파이 센서 키트](https://www.eleparts.co.kr/EPXDTWR8)  

## Python 예제 실행방법  

회로 연결은 Schematics 디렉토리의 이미지 파일 및 각 예제 상단의 GPIO 안내를 따라 해 주시면 됩니다.  

예제 실행은 각 예제를 `python3` 로 실행해 주시면 됩니다.

```bash
sudo python3 (예제 파일명).py
```

ex)

```bash
sudo python3 1.Ultrasonic sensor.py  
sudo python3 2.Passive Infrared Sensor.py  
...  
```

## 예제 코드 간단 설명  

### 1.Ultrasonic sensor  

초음파 센서 : 초음파를 발사, 정면에 있는 물체(장애물)과의 거리를 측정해 터미널로 출력해 줍니다.  

### 2.Passive Infrared Sensor (PIR sensor)  

디지털 적외선 물체 감지 센서 : 센서 정면 일정 범위의 움직임을 감지하여 LED를 ON 해 줍니다.  

### 3.Temp humidity sensor  

온습도 센서 : 온도&습도를 측정하여 터미널로 출력해 줍니다.  

DHT11 온습도 센서 사용을 위해 아래 라이브러리를 설치해 줍니다. (파이썬3)  

```bash
sudo pip3 install Adafruit_DHT  
```

pip가 설치되지 않은 경우 아래 명령어를 먼저 입력 해 주시면 됩니다.  

```bash
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
```

### 4.Analog Sound Sensor  

아날로그 사운드 센서  

### 5.Capacitive Touch Sensor  

디지털 정전식 터치센서  
