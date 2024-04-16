# Raspberry PI Sensor Kit  

[라즈베리파이 센서 키트](https://www.eleparts.co.kr/EPXDTWR8) 예제 코드 페이지입니다.  
  
## 라즈베리파이 5 사용 시 LGPIO 설치  
  
**라즈베리파이 5** 사용 시 아래 명령어로 **LGPIO**를 설치해 주어야 RPi.GPIO 라이브러리 사용이 가능합니다.  

```bash  
# 반드시 PI 5 사용시에만 설치
pip install --break-system-packages rpi-lgpio
```
  
Pi5가 아닌 경우 설치하면 분제가 발생할 수 있습니다.  
  
## Python 예제 실행방법  

회로 연결은 **Schematics 디렉토리의 이미지 파일** 및 각 **예제 상단의 GPIO 안내**를 따라 해 주시면 됩니다.  

예제 실행은 각 예제를 `python` 로 실행해 주시면 됩니다.

```bash
python (예제 파일명).py
```

ex)  

```bash
python 1.Ultrasonic sensor.py  
python 2.Passive Infrared Sensor.py  
...  
```

예제 종료는 **`CTRL + C`** 키를 눌러 주시면 됩니다.  

## 예제 코드 간단 설명  

### 1.Ultrasonic sensor  

초음파 센서 : 초음파를 발사, 정면에 있는 물체(장애물)과의 거리를 측정해 터미널로 출력해 줍니다.  

### 2.Passive Infrared Sensor (PIR sensor)  

디지털 적외선 물체 감지 센서 : 센서 정면 일정 범위의 움직임을 감지하여 LED를 ON 해 줍니다.  

### 3.Temp humidity sensor  
  
온습도 센서 : 온도&습도를 측정하여 터미널로 출력해 줍니다.  

DHT11 온습도 센서 사용을 위해서는 Adafruit_DHT 라이브러리를 설치해 주셔야 합니다.  

```bash
pip install --break-system-packages Adafruit_DHT  
```

### 3-1.Temp_humidity_sensor_pi5  
  
**PI5**에서 **Adafruit_DHT 라이브러리가 설치되지 않는 경우** 본 예제를 사용합니다.  
/boot/firmware/config.txt 파일에 아래 명령어를 추가해 줍니다.  
  
```bash
# /boot/firmware/config.txt 파일을 편집기로 열어 줍니다.
sudo nano /boot/firmware/config.txt

# config.txt 파일 맨 아래에 아래 옵션 추가
dtoverlay=dht11,gpiopin=21
```  

**저장 후 재부팅** 해 줍니다.  
재부팅 후 `ls /sys/bus/iio/devices` 명령어를 입력 시 `iio:device0`가 출력되어야 합니다.  
  
```bash
cat /sys/bus/iio/devices/iio:device0/in_humidityrelative_input  
cat /sys/bus/iio/devices/iio:device0/in_temp_input
```  

위 두 명령어로 간단하게 데이터를 출력 해 볼 수 있습니다. (소수점 아래 3자리까지 소수점 없이 출력됨)  
이후 예제 경로에서 `python 3-1.Temp_humidity_sensor_pi5.py`로 예제를 실행해 볼 수 있습니다.  
  
### 4.Analog Sound Sensor  

아날로그 사운드 센서 : 소리가 감지되면 잠시 LED를 켜 줍니다.  

### 5.Capacitive Touch Sensor  

디지털 정전식 터치센서 : 터치가 감지되면 LED를 켜 줍니다.  
