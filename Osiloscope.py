import pyvisa
from time import sleep
rm = pyvisa.ResourceManager()
print(rm.list_resources())
scope = rm.open_resource('USB0::0x0699::0x0405::C031998::INSTR')
scope.read_termination = '\n'
scope.write_termination = '\n'
scope.query_delay = 0.1


scope.query("*IDN?")
scope.write(":SELect:CH2 1")
#scope.enable_event()
scope.close()