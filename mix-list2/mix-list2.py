#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [22, 80, 443, 53] # a list of comman ports
proto.extend(proto2) # pass proto2 as an argument to the extended method -- then print result
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print results
print(protoa)
#proto.extend('dns') # this line will add 'd', 'n', and 's' to the end of the list
#print(proto)
