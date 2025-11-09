#!/usr/bin/env python3

# This relies on two points:
#  First, the counter class has a bug that stops the counter
#  changing if it is in the default step down mode.  This
#  means the keystream is just a repeating 16 bytes.
#  Second, pngs always start with the same 16 bytes, allowing
#  us to recover the first 16 bytes of the keystream.

from urllib.request import urlopen
from itertools import cycle
import json

url = 'https://aes.cryptohack.org/bean_counter/'
png_header_hex = '89504e470d0a1a0a0000000d49484452'
png_header = bytes.fromhex(png_header_hex)


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


response = json.loads(urlopen(url + 'encrypt/').read())
ciphertext = bytes.fromhex(response['encrypted'])
key = xor(ciphertext, png_header)
plaintext = xor(ciphertext, cycle(key))

open('bean_flag.png', 'wb').write(plaintext)
