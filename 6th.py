from collections import Counter

cipher = input("Ciphertext: ")
print(Counter(cipher).most_common())
