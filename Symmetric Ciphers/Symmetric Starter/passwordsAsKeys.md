# Utilisation de mots de passe comme clés pour AES

Ce script Python tente de déchiffrer un texte chiffré avec AES en mode ECB, en utilisant une liste de mots comme clés potentielles. Chaque mot est transformé en clé AES via le hachage MD5. Si le texte déchiffré contient le mot `crypto`, le script affiche le texte en clair et la clé utilisée.

```python
from Crypto.Cipher import AES
import hashlib

ciphertext = bytes.fromhex('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')

# Lecture de la liste de mots
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for w in words:
    # Génération de la clé AES à partir du mot de passe (MD5)
    key = hashlib.md5(w.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)

    # Vérification si le texte déchiffré contient 'crypto'
    if b'crypto' in decrypted:
        print("plaintext", decrypted)
        print("password_hash", key.hex())
        exit
```

**Explications :**
- On lit tous les mots du fichier `words.txt`.
- Chaque mot est converti en clé AES de 16 octets grâce à MD5.
- On tente de déchiffrer le texte chiffré avec chaque clé.
- Si le texte déchiffré contient `crypto`, on affiche le résultat et la clé.