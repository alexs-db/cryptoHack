#!/usr/bin/env python3
# minimal byte-at-a-time ECB recover (handles "min 16 A" constraint)
# pip install requests

import requests
from binascii import hexlify, unhexlify

BASE_URL = "http://aes.cryptohack.org"   # <-- change this
ENDPOINT = "/ecb_oracle/encrypt/{hex}/"
B = 16

def ask(b: bytes) -> bytes:
    h = hexlify(b).decode()
    url = BASE_URL.rstrip("/") + ENDPOINT.format(hex=h)
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return bytes.fromhex(r.json()["ciphertext"])

def make_prefix(n_recovered: int) -> bytes:
    pad_len = (B - (n_recovered % B) - 1)
    while pad_len < B:
        pad_len += B
    return b"A" * pad_len

def recover(max_bytes=200):
    recovered = b""
    while len(recovered) < max_bytes:
        n = len(recovered)
        prefix = make_prefix(n)
        block_idx = (len(prefix) + n) // B
        start = block_idx * B
        ct = ask(prefix)
        if len(ct) < (block_idx+1)*B:
            print("Unexpected ciphertext length; abort.")
            break
        target = ct[start:start+B]

        found = False
        # printable first
        for c in range(32,127):
            trial = prefix + recovered + bytes([c])
            ct2 = ask(trial)
            if ct2[start:start+B] == target:
                recovered += bytes([c])
                print("FOUND:", recovered.decode(errors="replace"))
                found = True
                break
        if found:
            continue
        # full 0..255 fallback
        for c in range(0,256):
            trial = prefix + recovered + bytes([c])
            ct2 = ask(trial)
            if ct2[start:start+B] == target:
                recovered += bytes([c])
                print("FOUND (bin):", recovered)
                found = True
                break
        if not found:
            print("No byte matched — likely end of flag. Recovered:", recovered)
            break
    return recovered

if __name__ == "__main__":
    flag = recover(512)
    try:
        print("FLAG:", flag.decode())
    except:
        print("FLAG (hex):", hexlify(flag).decode())
