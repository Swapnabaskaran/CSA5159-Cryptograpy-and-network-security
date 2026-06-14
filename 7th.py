plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "cipherabdfgjklmnoqstuvwxyz"

def encrypt(text):
    return ''.join(cipher[plain.index(c)] if c in plain else c for c in text)

def decrypt(text):
    return ''.join(plain[cipher.index(c)] if c in cipher else c for c in text)

msg = input("Text: ").lower()

c = encrypt(msg)
print("Cipher:", c)
print("Plain :", decrypt(c))
