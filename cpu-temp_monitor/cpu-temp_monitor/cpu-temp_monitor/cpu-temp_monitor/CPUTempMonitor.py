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






#USE BELOW FOR REFERENCE 


#average the temp of CPU among cores
#total = 0
#
#sensorsToMonitor = []

#get sensors for temp, we find the sensors to poll from only once by scanning all available sensors.
#for a in range(0, len(c.Hardware[0].Sensors)):
#    print(c.Hardware[0].Sensors[a].Identifier) #use to see sensor identifiers
#    if "temperature" in str(c.Hardware[0].Sensors[a].Identifier):
#        sensorsToMonitor.append(a)
#   
#while True:
#
#    for b in range(0, len(sensorsToMonitor)):
#        total = total + c.Hardware[0].Sensors[b].get_Value()
#        c.Hardware[0].Update()
#        print(b)
#            
#    print(str(total/len(sensorsToMonitor)) + "C")
#    total = 0
    
