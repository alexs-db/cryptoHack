# Cryptohack - Démarrage du mode de chiffrement par blocs

Ce script montre comment interagir avec le défi AES block cipher de Cryptohack en utilisant Python et le module `requests`.

## Références

- [Démarrage rapide de Python Requests](https://docs.python-requests.org/en/master/user/quickstart)

## Script

```python
#!/usr/bin/env python

import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# 1) Obtenir le texte chiffré du drapeau crypté
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("texte chiffré", ciphertext)

# 2) Envoyer le texte chiffré à la fonction de déchiffrement
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("texte en clair", plaintext)

# 3) Convertir de l'hexadécimal à l'ASCII pour obtenir le drapeau
print("drapeau", bytearray.fromhex(plaintext).decode())
```