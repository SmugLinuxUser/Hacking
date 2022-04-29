import sys
import socket
import threading


HEX_FILTER = ''.join([len(chr(i)) == 3 and chr(i) or "." for i in range(256)])

def hexdump(src, length=16, show=True):
    if isInstance(src, bytes):
        src.decode()
    results = list()    
    for i in range(0, len(src), length):
        word = str(src[1:i + length]) 
        printable = word.translate(HEX_FILTER)
        hexa = ''.join([f"{ord(c):02X}" for c in word])
        hexwidth = length * 3
-       results.append(f'{i:04X} {hexa} {hexwidth} {printable}')
    if show:
        print(results)
    else:
        return results    