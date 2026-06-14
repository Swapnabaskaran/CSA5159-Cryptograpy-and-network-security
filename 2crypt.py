p = "abcdefghijklmnopqrstuvwxyz"
c = "qwertyuiopasdfghjklzxcvbnm"

msg = input("Text: ").lower()

enc = ''.join(c[p.index(x)] if x in p else x for x in msg)

print("Cipher:", enc)
