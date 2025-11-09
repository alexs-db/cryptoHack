import requests
from Crypto.Util.strxor import strxor
from binascii import unhexlify

BASE_URL = "https://aes.cryptohack.org/ecbcbcwtf"

# 1. Obtenir le ciphertext (IV + CBC encrypted FLAG)
resp = requests.get(f"{BASE_URL}/encrypt_flag/").json()
ciphertext = bytes.fromhex(resp["ciphertext"])

# 2. Découper en blocs de 16 octets
blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

flag = b""
for i in range(1, len(blocks)):  # C1, C2, ...
    # 3. Déchiffrer Ci avec l’oracle ECB
    dec_resp = requests.get(f"{BASE_URL}/decrypt/{blocks[i].hex()}/").json()
    D_Ci = bytes.fromhex(dec_resp["plaintext"])
    
    # 4. Reconstituer Pi = D(Ci) ⊕ C(i-1)
    Pi = strxor(D_Ci, blocks[i-1])
    flag += Pi

print("FLAG:", flag.decode())
