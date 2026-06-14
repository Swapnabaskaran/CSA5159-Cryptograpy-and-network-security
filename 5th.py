from math import gcd

for a in range(26):
    if gcd(a,26)==1:
        for b in range(26):
            if (a*4+b)%26==1 and (a*19+b)%26==20:
                print("a =",a,"b =",b)
