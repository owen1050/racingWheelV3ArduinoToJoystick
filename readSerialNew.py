import time
import serial
import pyvjoy
import math
import sys
import numpy as np
sw = 0 #a8
swRaw = 0
swMin = 512 #right turn
swMax = 1017 #left turn

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

                    if abs(gasBreakRaw - breakGasMid) > 3:
                        if(gasBreakRaw < breakGasMid):
                            gasPRaw = 0
                            breakPRaw = breakGasMid - gasBreakRaw #0 to 150
                        else:
                            breakPRaw = 0
                            gasPRaw = gasBreakRaw - breakGasMid #0 to 298
                    else:
                        gasPRaw = 0
                        breakPRaw = 0

                    print(gasPRaw, breakPRaw, swRaw, L1, L2, R1, R2)
                    
                    j.data.wAxisZ = int(0)
                    j.data.wAxisX = int(0)
                    j.data.wAxisY = int(0)
                    
                    j.update()
        except: 
                print("error")
                