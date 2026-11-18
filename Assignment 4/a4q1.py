from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

plaintext = b"This assignment is the fourth out of six assignments in the course COMP 755."
# Generate random 8-byte (64-bit) DES key
key = os.urandom(8)
iv = os.urandom(8)

cipher = DES.new(key, DES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

print("Key (hex):", key.hex().upper())
print("IV (hex):", iv.hex().upper())
print("Ciphertext (hex):", ciphertext.hex().upper())
