from pwn import *


KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2 = ''
KEY3 = ''
FLAG = ''

resultK1K2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
resultK2K3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
resultK3K2K1Flag = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'


Key1Final = bytes.fromhex(KEY1)
resultK1K2Final = bytes.fromhex(resultK1K2)
resultK2K3Final = bytes.fromhex(resultK2K3)
resultK3K2K1FlagFinal = bytes.fromhex(resultK3K2K1Flag)



KEY2 = xor(Key1Final, resultK1K2Final)


KEY3 = xor(KEY2, resultK2K3Final)



FLAG = xor(KEY3, KEY2, Key1Final, resultK3K2K1FlagFinal)


print(FLAG)
