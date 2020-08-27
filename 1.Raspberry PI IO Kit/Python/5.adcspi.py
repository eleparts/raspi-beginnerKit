"""
* 라즈베리파이 입출력 키트 추가 ADC 구동 예제 05.adcspi 
* 
* 본 예제는 MCP3204 ADC IC를 추가로 연결해 아날로그 신호(가변저항 이용)을 입력받아 터미널창에 출력(0~4095, 12bit)해 줍니다.
*
* 사용 소자 : MCP3204 ADC IC, 가변저항
* MCP3204 ADC IC
* VDD(14), VREF(13) : 3.3V | DGND(7), AGND(12) : GND
* CLK(11)    : GPIO 23번 (SPI_CLK)
* DOUT(10)   : GPIO 21번 (SPI_MISO)
* DIN(8)     : GPIO 19번 (SPI_MOSI)
* CS/SHDN(8) : GPIO 24번 (SPI_CE0_N)
* CH0~3(1~4) : ADC 입력 
*
* 가변저항  
* 양 끝단은 각각 VCC(3.3V)/ GND에 연결, 중앙 핀은 MCP3204의 CHx(1~4) 핀으로 연결해 줍니다.
*
* 라즈베리파이의 SPI 통신 기능을 사용하므로 라즈베리파이 설정(raspi-config)에서 SPI를 Enable 해 주셔야 합니다.
*
* 키트 정보 : https://www.eleparts.co.kr/EPXDTWPM
* MCP3204  : https://www.eleparts.co.kr/EPX3AHC4
* MCP3204 데이터시트 : https://www.farnell.com/datasheets/808967.pdf
"""
# MCP3204/3208, 12bit ADC, SPI

import spidev
import time

spi=spidev.SpiDev()          # SPI 입력을 위해 SpiDev() 사용
spi.open(0,0)
spi.max_speed_hz=1000000
spi.bits_per_word=8


def spi_read(channel=0,sglDiff=1):    # MCP320x SPI 데이터 수신 함수
  
  if(7 < channel or 0 > channel) or (sglDiff < 0 or sglDiff > 1):
    return -1

  # start High + 4bit 송신, 1clock 후 LOW + 12bit data 수신
  startBit = 0x04
  sglDiff  = sglDiff * 0x02
  D2 = int((channel/4)%2) * 0x01
  D1 = int((channel/2)%2) * 0x80
  D0 = int((channel)%2) * 0x40

  send1 = startBit + sglDiff + D2
  send2 = D1 + D0

  data = spi.xfer2([send1,send2,0,0])
  adcValue = ((data[1] & 0x0F) << 8) + data[2]

  return adcValue


try:
  while 1:
    
    # ADC 각 채널별로 터미널창에 출력
    print("ch0 : %d", spi_read(0))
    print("ch1 : %d", spi_read(1))
    print("ch2 : %d", spi_read(2))
    print("ch3 : %d", spi_read(3))
    print("-----------------")
    time.sleep(0.1)

finally:
  spi.close()       # SPI 종료
