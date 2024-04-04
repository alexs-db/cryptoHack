string = 'label'
numb = 13
result = ''

for char in string:
    xor_result = ord(char) ^ numb
    result += chr(xor_result)

flag = 'crypto{' + result + '}'
print(flag)
