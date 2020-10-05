import serial
import pyvisa
from time import sleep

'''Power Supply 통신 설정'''
port = "COM3" #통신 포트 선택
baud = 9600    #Baud Rate 설정
power_supply = serial.Serial(port, baud, timeout=1)

'''DMM 통신 설정'''
rm = pyvisa.ResourceManager()
#print(rm.list_resources())
dmm = rm.open_resource('USB0::0x05E6::0x6510::04463353::INSTR')
dmm.read_termination = '\n'
dmm.write_termination = '\n'
dmm.query_delay = 0.1

'''명령어 동작 확인
power_supply.write('*IDN?\n'.encode())  #command 입력
print(power_supply.readline())          #수신 데이터 확인
print(dmm.query('*IDN?'))
'''
'''변수설정'''
chanel='2'
volt=['5.5','1.8']

'''동작전류 측정'''
for v in volt:
    command = ':CHANnel'+chanel+':VOLTage '+v+'\n'
    power_supply.write(command.encode())
    power_supply.write(':OUTPut:STATe 1\n'.encode())
    sleep(0.5)
    result = dmm.query(":MEASure:CURRent:DC?")
    print(result)

'''통신 종료'''
power_supply.close()
dmm.close()
