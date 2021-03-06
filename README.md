# raspi-beginnerKit  

엘레파츠의 라즈베리파이 [**입출력 키트(I/O Kit)**](https://www.eleparts.co.kr/EPXDTWPM) 및 [**센서 키트(Sensor Kit)**](https://www.eleparts.co.kr/EPXDTWR8)의 예제 코드 GitHub 페이지 입니다.  

키트별 예제 실행방법에 대한 상세 설명은 **[키트]**-> **[언어(C/Python)]** 페이지에 다시 안내되어 있습니다.  

## 예제 코드 사용을 위한 준비사항  

라즈베리파이 업데이트  

```bash
sudo apt-get update && sudo apt-get upgrade  
```

예제 코드 다운로드 **(라즈베리파이 터미널에서 실행)**  

```bash
git clone https://github.com/eleparts/raspi-beginnerKit  
cd raspi-beginnerKit
ls -l
```

위 디렉토리에서 사용할 예제 디렉토리로 이동해 주시면 됩니다.  

### > C언어  

C언어 예제 실행을 위해서는 wirringPi 라이브러리 설치가 필요합니다.  

소스 관리 툴(git)다운로드 및 WiringPi 설치  

```bash
sudo apt-get install git-core  

git clone https://github.com/WiringPi/WiringPi  
cd WiringPi  
./build  
```

wirringPi 설치 확인 및 GPIO 번호 출력  

```bash
gpio readall  
```

- WiringPi가 공식적으로 지원을 중단함으로 인해 비공식 미러 페이지를 사용합니다.  [(관련 공지 URL)](http://wiringpi.com/wiringpi-deprecated/)  

### > 파이썬  

python3는 아래 명령어로 설치가 가능합니다.  
다만, 라즈베리파이(라즈비안)에는 파이썬 3가 설치되어 있기 때문에 설치 과정은 생략해도 무관합니다.  

```bash
sudo apt-get install python3  
```

## 입출력 키트 추가 구성 상품 안내  

입출력(I/O) 키트의 가변저항을 이용한 아날로그 입력 기능을 위한 ADC IC (별매) 링크입니다.  

[MCP3204 ADC IC](https://www.eleparts.co.kr/EPX3AHC4)  

해당하는 예제는 [I/O키트] -> [5.adcspi] 입니다.  

## 엘레파츠 입출력 & 센서 키트 바로가기  

[라즈베리파이 입출력(I/O) 키트](https://www.eleparts.co.kr/EPXDTWPM)  

[라즈베리파이 센서 키트](https://www.eleparts.co.kr/EPXDTWR8)  

## 추가 자료 - 네이버 블로그  

기존 블로그 자료 URL입니다.  

### 입출력 키트(I/O Kit)  

[라즈베리파이 입출력 키트 GPIO 제어하기-1](https://blog.naver.com/elepartsblog/220284169123)  

[라즈베리파이 입출력 키트 GPIO 제어하기-2](https://blog.naver.com/elepartsblog/220285369508)  

### 센서 키트  

[라즈베리파이 센서 키트 - 초음파 센서 제어하기](https://blog.naver.com/elepartsblog/220288246775)  

[라즈베리파이 센서 키트 - 적외선 물체 감지 센서/터치센서 제어하기](https://blog.naver.com/elepartsblog/220294594150)  
