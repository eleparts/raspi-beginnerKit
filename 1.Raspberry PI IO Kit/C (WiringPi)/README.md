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

GPIO 번호 확인

```bash
gpio readall  
```
  
- WiringPi가 공식적으로 지원을 중단함으로 인해 비공식 미러 페이지를 사용합니다.  [(관련 공지 URL)](http://wiringpi.com/wiringpi-deprecated/)  
  
## C언어 예제 실행방법  

회로 배선은 예제 상단의 GPIO 맵 및 Schematics 디렉토리의 이미지 파일을 따라 해 주시면 됩니다.  

각 예제 디렉토리에서 아래와 같이 컴파일&실행해 주시면 됩니다.  

```bash
gcc -o main main.c -lwiringPi

sudo ./main
```
