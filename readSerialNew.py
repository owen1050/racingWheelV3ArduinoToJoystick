import time
import serial
import pyvjoy
import math
import sys
import numpy as np
sw = 0 #a8
swRaw = 0
swMin = 501 #right turn
swMax = 1017 #left turn
swMid = 662

gasP = 0#higher half of a9
breakP = 0#lower half of a9
gasPRaw = 0
breakPRaw = 0
gasBreakRaw = 0
breakMin = 587 #mid is 733
breakGasMid = 720
gasMax = 1018

L1 = False #a1
L1T = 450 #pressed is less than this
L1Raw = 0
L2Raw = 0
L2 = False #a2
L2T = 450 #pressed is less than this

R1 = False #A10
R1T = 800 #pressed is more than this
R1Raw = 0
R2Raw = 0
R2 = False #A11
R2T = 750 #pressed is more than this

buttSum = 0

ser = serial.Serial('COM7', 250000, timeout=0)
j = pyvjoy.VJoyDevice(1)
while 1:
    

        try:
                if ser.inWaiting()>68:
                    a = str(ser.readline())         
                    #print(a)
                    i0 = a.find("A2:")+3
                    i1 = a.find("!",i0)
                    L2Raw = int(a[i0:i1])
                    

                    i0 = a.find("A1:")+3
                    i1 = a.find("!",i0)
                    L1Raw = int(a[i0:i1])

                    i0 = a.find("A11:")+4
                    i1 = a.find("!",i0)
                    R2Raw = int(a[i0:i1])
                    

                    i0 = a.find("A10:")+4
                    i1 = a.find("!",i0)
                    R1Raw = int(a[i0:i1])

                    i0 = a.find("A8:")+3
                    i1 = a.find("!",i0)
                    swRaw = int(a[i0:i1])

                    i0 = a.find("A9:")+3
                    i1 = a.find("!",i0)
                    gasBreakRaw = int(a[i0:i1])

                    L1 = L1Raw < L1T
                    L2 = L2Raw < L2T

                    R1 = R1Raw > R1T
                    R2 = R2Raw > R2T

                    buttSum = 0

                    buttSum += 1 * L1
                    buttSum += 2 * L2
                    buttSum += 4 * R1
                    buttSum += 8 * R2

                    if abs(gasBreakRaw - breakGasMid) > 3:
                        if(gasBreakRaw < breakGasMid):
                            gasPRaw = 0
                            breakP = (breakGasMid - gasBreakRaw) * 213 #0 to 150
                        else:
                            breakPRaw = 0
                            gasP = (gasBreakRaw - breakGasMid) * 107 #0 to 298
                    else:
                        gasP = 0
                        breakP = 0

                    if(abs(swRaw - swMid) > 2):
                        if(swRaw > swMid):
                            swTemp = swMax - swRaw
                            sw = swTemp * 47
                        else:
                            swTemp = swMid - swRaw
                            sw = (swTemp * 99) + 16000
                    else:
                        sw = 16000


                    #sw calc 0 to 16000 == 1007 to 670
                    #1007 - raw gives 0 to 337
                    #multiple by 47
                    #16000 to 32000 == 670 to 512
                    #670- raw givces 0 to 158
                    # that *102 +_ 16000



                    print(gasP, breakP, sw, L1, L2, R1, R2)
                    
                    j.data.wAxisZ = int(sw)
                    j.data.wAxisX = int(gasP)
                    j.data.wAxisY = int(breakP)

                    j.data.lButtons = buttSum

                    j.update()
        except: 
                print("error")
                