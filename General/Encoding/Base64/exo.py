import base64 #module


numb = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

test = bytes.fromhex(numb)

print(test)

flag = base64.b64encode(test) 

print(flag)
