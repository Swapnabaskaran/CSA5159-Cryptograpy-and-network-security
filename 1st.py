from collections import Counter
import string

# Create plaintext file
with open("plaintext.txt", "w") as f:
    f.write("helloworldthisisamonoalphabeticcipherexample")

plain = string.ascii_lowercase
cipher = "qwertyuiopasdfghjklzxcvbnm"

enc = str.maketrans(plain, cipher)
dec = str.maketrans(cipher, plain)

with open("plaintext.txt", "r") as f:
    text = f.read().lower()

ciphertext = text.translate(enc)

with open("ciphertext.txt", "w") as f:
    f.write(ciphertext)

print("Plain Frequency:", Counter(text))
print("Cipher Frequency:", Counter(ciphertext))
print("Decrypted:", ciphertext.translate(dec))
