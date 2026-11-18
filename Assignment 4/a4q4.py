from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

plaintext = b"This assignment is the fourth out of six assignments in the course COMP 755."

# Generate 2048-bit RSA key pair
key_pair = RSA.generate(2048)
public_key = key_pair.publickey()

cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(plaintext)

print("Modulus Size:", key_pair.size_in_bits(), "bits")
print("Ciphertext (hex):", ciphertext.hex().upper())
