from math import gcd

def affine_encrypt(text, a, b):
    if gcd(a,26)!=1:
        return "Invalid a"
    return ''.join(chr(((a*(ord(c)-97)+b)%26)+97) for c in text)

msg = input("Text: ")
a = int(input("a: "))
b = int(input("b: "))

print("Cipher:", affine_encrypt(msg,a,b))
