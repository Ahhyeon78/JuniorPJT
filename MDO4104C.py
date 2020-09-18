import pyvisa

rm = pyvisa.ResourceManager()
#print(rm.list_resources())
mdo4104 = rm.open_resource('USB0::0x0699::0x0405::C031998::INSTR')

print(mdo4104.query("*IDN?"))
mdo4104.write(":SELect:CH2 1")