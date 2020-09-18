import serial

port = "COM11" #통신 포트 선택
baud = 9600    #Baud Rate 설정
pst3202 = serial.Serial(port, baud, timeout=1)

if pst3202.isOpen():
     print(pst3202.name + ' is open...')

pst3202.write('*IDN?\n'.encode())  #command 입력
print(pst3202.readline())          #수신 데이터 확인

'''
pst3202.write(':CHANnel1:CURRent 0.5\n'.encode('ascii'))

pst3202.write(':OUTPut:STATe 1\n'.encode())

#out = str(pst3202.readlines())
print(pst3202.write(':CHANnel1:CURRent?\n'.encode()))
print(pst3202.write(':CHANnel3:MEASure:VOLTage ?'.encode()))
pst3202.write(':OUTPut:STATe 0\n'.encode())
'''
pst3202.close()
if not(pst3202.isOpen()):
     print(pst3202.name + ' is close...')
'''
-------General Setting Commands-----------
:CHANnel<x>:CURRent <NR2> ★1 Sets the value of current.
:CHANnel<x>:CURRent ? ★1 Return the value of current.
:CHANnel<x>:VOLTage <NR2> ★1 Sets the value of voltage.
:CHANnel<x>:VOLTage ? ★1 Return the value of voltage.
:CHANnel<x>:MEASure:CURRent ? ★1 Returns actual output current.
:CHANnel<x>:MEASure:VOLTage ? ★1 Returns actual output voltage.
:CHANnel<x>:PROTection:CURRent<Boolean>★1 Sets the over current protection(OCP) on or off.
:CHANnel<x>:PROTection:CURRent ? ★1 Returns the state of the overcurrent protection (OCP) setting as either on or off.
:CHANnel<x>:PROTection:VOLTage <NR2> ★1 Sets the value of overvoltage protection (OVP).
:CHANnel<x>:PROTection:VOLTage ? ★1 Returns the overvoltage protection (OVP) setting.
:OUTPut:COUPle:TRACking <NR1> ★2 Sets the output of the power supply working on Seriestracking or Parallel-tracking or independent mode.
:OUTPut:COUPle:TRACking ? ★2 Returns the output of the power supply working mode.
:OUTPut:PROTection:CLEar Clears over-voltage and over-current and over temperature protection error message.
:OUTPut:STATe <Boolean> Sets the output state on or off.
:OUTPut:STATe ? Returns the output state on or off.

-------Status Commands---------------------
*CLS Clears the status data structures.
*ESE <NR1> Sets the Event Status Enable Register(ESER).
*ESE? Returns contents of Event Status Enable Register (ESER).
*ESR? Returns and clear the contents of Standard Event Status Register (SESR).
*SRE <NR1> Sets contents of Service Request Enable Register(SRER).
*SRE? Returns contents of Service Request Enable Register (SRER).
*STB? Reads Status Byte Register (SBR).
:STATus:OPERation:CONDition ? Returns the contents of the OPERation condition register. Returns NR1.
:STATus:OPERation:ENABle <NR1> Sets the contents of the enable mask for the OPERation event register.
:STATus:OPERation:ENABle ? Returns the contents of the enable mask for the OPERation event register. Returns NR1.
:STATus:OPERation:EVENt ? Query the contents of the OPERation Event register.
:STATus:PRESet Presets the OPERation and QUEStionable status registers.
:STATus:QUEStionable:CONDition ? Returns the contents of the OPERation condition register. Returns NR1.
:STATus:QUEStionable:ENABle <NR1> Sets the contents of the enable mask for the QUEStionable enable register.
:STATus:QUEStionable:ENABle ? Query the contents of the Questionable Enable register.
:STATus:QUEStionable:EVENt ? Query the contents of the QUEStionable Event register.

--------Miscellaneous Commands-------------
*IDN? Returns instrument identification.
*OPC Reports when operation is complete by setting the Operation Complete bit in SESR.
*OPC? Reports when operation is complete. Same as
*OPC except returns a 1 to the output queue and dose not set the SESR bit.
*RCL ★Recall the setting data from the memory which previous saved.
*RST Resets the protection levels and states, resets the current and voltage levels to zero, sets the output off, and sets memory section to 00.
*SAV ★Saves the setting data to memory.
*TST? Initiates internal self-test and reports results.
*WAI Wait to continue. This command forces sequential operation of commands. This command is required by IEEE-488.1-1987.
The power supply, however, forces sequential operation of commands by design.
:SYSTem:AUTO:CYCLe<NR1> ★Set number of times of execution.
:SYSTem:AUTO:CYCLe ? ★Query the setting of the number of times of execution.
:SYSTem:AUTO:DELay<NR1> ★ Set the delay time under the current responding memory status.
:SYSTem:AUTO:DELay ? ★Query the setting of the delay time under the current responding memory status.
:SYSTem:AUTO:END<NR1> ★ Set the end memory section for auto execute continuously.
:SYSTem:AUTO:END ? ★Query the end memory section for auto execute continuously.
:SYSTem:AUTO:STARt<NR1> ★ Set the start memory section for auto execute continuously.
:SYSTem:AUTO:STARt ? ★Query the start memory section for auto execute continuously.
:SYSTem:AUTO:STATe<Boolean> ★Sets Auto sequence on or off.
:SYSTem:AUTO:STATe ? ★Returns Auto Sequence mode on or off.
:SYSTem:ERRor ? Read the next item from the error/event queue.
:SYSTem:MEMory? ★Query the last memory location
:SYSTem:VERSion? Returns the SCPI version level.
'''