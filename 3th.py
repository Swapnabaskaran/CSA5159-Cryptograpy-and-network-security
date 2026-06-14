def caesar(t,k):
    return ''.join(chr((ord(c)-97+k)%26+97) for c in t)

msg=input("Text:")
k=int(input("Key:"))
c=caesar(msg,k)
print("Cipher:",c)
print("Plain :",caesar(c,-k))
