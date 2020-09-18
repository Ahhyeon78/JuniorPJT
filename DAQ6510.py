import pyvisa

rm = pyvisa.ResourceManager()
#print(rm.list_resources())
daq6510 = rm.open_resource('USB0::0x05E6::0x6510::04463353::INSTR')
print(daq6510.query("*IDN?"))

daq6510.write("*rst; status:preset; *cls") #초기화 및 재설정 메시지
#daq6510.write(":MEASure:CURRent:DC?")
print(daq6510.query(":MEASure:CURRent:DC?"))

daq6510.close()