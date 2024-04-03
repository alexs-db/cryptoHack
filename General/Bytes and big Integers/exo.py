from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

hexa = hex(integer)

print (hexa)

hexa2 = int(hexa, 16)

hexBytes = long_to_bytes(hexa2)

print(hexBytes)