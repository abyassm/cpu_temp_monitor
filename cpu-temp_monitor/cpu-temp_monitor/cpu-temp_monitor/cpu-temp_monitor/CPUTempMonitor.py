import os
import time
import clr # the pythonnet module.
currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)
clr.AddReference(currentPath +  "\OpenHardwareMonitorLib.dll")
from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()

sensorToPoll = 0
intervalInSeconds = 0.5

# clear terminal, works on unix and windows
def clear():
    
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')




#find first temp sensor, usually is all core average
for a in range(0, len(c.Hardware[0].Sensors)):
    print(c.Hardware[0].Sensors[a].Identifier) #use to see sensor identifiers
    if "temperature" in str(c.Hardware[0].Sensors[a].Identifier):
        sensorToPoll = a
        break
   
while True:
        #keep printing temp
        clear()
        print("Temperature:")
        print(str(c.Hardware[0].Sensors[sensorToPoll].get_Value()) + "C")
        c.Hardware[0].Update()
        time.sleep(intervalInSeconds)



    
