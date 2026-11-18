from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import os

plaintext = b"This assignment is the fourth out of six assignments in the course COMP 755."
# Generate random 24-byte (192-bit / 3-key) 3DES key
key = DES3.adjust_key_parity(os.urandom(24))
iv = os.urandom(8)

cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

print("3DES Key (hex):", key.hex().upper())
print("Ciphertext (hex):", ciphertext.hex().upper())
