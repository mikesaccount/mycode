#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') # this line prompts the user for input

if ipchk == '192.168.1.1': 
    print('Looks like the Default Gateway IP was set: ' + ipchk) # indented under if
elif ipchk: # if data is NOT provided
    print(' Looks like IP address was set')
else:
    print('You did not provide input.') # indented under else
