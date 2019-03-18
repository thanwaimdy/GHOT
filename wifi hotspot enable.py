
#!/usr/bin/python3
# wifi hotspot enabler
# AungWinnHtut GHOT

import os
os.system('cls')
print('\n\n\n')
print('Green Hacker WiFI Hotspot Enabler')
print('(c) 2019 Green Hackers Group. All right reserved')
print()

cmd = '0' # space is very caution between cmd and = , if not ssid and key are mixed.

while cmd != '3':
    print('1-Start Hotspot')
    print('2-Stop Hotspot')
    print('3-Exit')
    cmd = input('Please Enter Your Choice (1,2,3):  ')
    if cmd == '1':
        print('Starting Wifi Hotspot....')
        ssid = input('Please Enter SSID: ')
        password = input('Please Enter Password: ')
        command = " netsh wlan set hostednetwork mode = allow ssid= " + ssid + " key= " + password
        os.system(command)
        os.system('netsh wlan start hostednetwork')
    elif cmd == '2':
        print('Stopping Wifi Hotspot....')
        os.system('netsh wlan stop hostednetwork')
    elif cmd == '3':
        print('Exit Program....')
        quit()
    else:
        print("Bad input! Please try again (Only 1,2,3)")
        os.system('pause')

# now run this code but it was run in administrator mode.
#  os.system("netsh wlan set hostednetwork mode=allow ssid=GreenHackers key=12345678")
#  os.system('netsh wlan start hostednetwork')
# now all are OK after cmd='0'
# DONE! 15/3/2019 12:22AM, Thanks Sir AgWinnHtut. 

