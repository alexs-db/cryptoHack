numb = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
byteVar = bytes.fromhex(numb)
result = ""

for byte in range(256):  # There are 256 possible bytes
    decoded = ""
    for i in range(len(byteVar)):
        xor_result = byteVar[i] ^ byte
        decoded += chr(xor_result)
    print(f"With byte {byte:02x}: {decoded}")

