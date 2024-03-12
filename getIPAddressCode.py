#Date:
#Author :
#Purpose: To know os version and run the ping command
import platform
import os


print(platform.machine())
print(platform.platform())  # Will help you to find the underlying OS

if 'Windows' in platform.platform():
    print ("It's a windows platform")
    cmdStr =  "ipconfig"
    retrnVal = os.popen(cmdStr).read()
    if '164' in retrnVal or '169' in retrnVal:
        print ("It's in the range")
    else:
        print ("It's not in the range")
    

elif 'linux' in platform.platform():
    print ("It's Linux Platform")
    cmdStr = "ifconfig"
    retrnVal = os.popen(cmdStr).read()
    print(retrnVal)
else:
    print("It's a mac")
    
    
