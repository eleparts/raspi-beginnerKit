/*
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
*/
// MCP3204/3208, 12bit ADC, SPI

#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>

#define CHANNEL 0             // SPI_CE0_N 사용(SPI 0번 채널)
#define SPEED 1000000


int spi_read(int channel){    // MCP320x SPI 데이터 수신 함수

    unsigned char data[3] = {0,};
    int adcValue = 0;
    int startBit, sglDiff, D0, D1, D2;

    // start High + 4bit 송신, 1clock 후 LOW + 12bit data 수신
    startBit = 0x04;
    sglDiff  = 0x02;
    D2 = ((channel/4)%2) * 0x01;
    D1 = ((channel/2)%2) * 0x80;
    D0 = ((channel)%2) * 0x40;

    data[0] = startBit + sglDiff + D2;
    data[1] = D1 + D0;

    wiringPiSPIDataRW(CHANNEL, data, 3);

    data[1] = 0x0F & data[1];
    adcValue = ((data[1] & 0x0F) << 8) + data[2];

    return adcValue;
}


int main (void){

    if(wiringPiSetup() == -1)
        return -1;

    if(wiringPiSPISetup(CHANNEL, SPEED) == -1)    // SPI 설정
        return -1;

    printf("Raspberry PI ADC Test(MCP3204/3208)\r\n");

    while(1){

        // ADC 각 채널별로 터미널창에 출력
        printf("ch0 : %d\r\n", spi_read(0));
        printf("ch1 : %d\r\n", spi_read(1));
        printf("ch2 : %d\r\n", spi_read(2));
        printf("ch3 : %d\r\n", spi_read(3));
        printf("-----------------\r\n");
        delay(100);
    }

    return 0;
}