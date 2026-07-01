#!/bin/python3

import base64
import binascii

base64Str = "MkMyODIyMzEwOTE2NEI0MzFFMDQwRTNFMDAxMDVCNUUwRTBFMTQxMjBG"
userDecoded = "Jacare20"

def xor(b1, b2):

    b2 = b2 * (len(b1) // len(b2)) + b2[:len(b1) % len(b2)]

    print(b1, b2)
    
    # XOR
    xorByte = bytes(a ^ b for a, b in zip(b1, b2))
    xorHex = xorByte.hex()
    xorAscii = ''.join(chr(b) if 32 <= b <= 126 else '' for b in xorByte)

    return xorByte, xorHex, xorAscii

hex1 = base64.b64decode(base64Str)
hex2 = binascii.hexlify(userDecoded.encode())

#print(hex1, userEncoded)
print(xor(hex1, hex2))
