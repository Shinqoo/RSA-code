from math import gcd


def encryption(p, q, str):
    
    n = p*q
    z = (p-1)*(q-1)
    encrypt = ""
    
    for e in range(1, n+1):
        if z % e !=  0 and n-1 % e != 0:
            break;
            
    for d in range(1, z+1):
        if ((e*d)-1) % z ==  0:
            break;  
            
    for i in str:
        m = pow(ord(i),e)%n
        encrypt += chr(m)
    
    return encrypt
    
def decryption(p, q, word):
    
    n = p*q
    z = (p-1)*(q-1)
    decrypt = ""
    
    for e in range(1, n+1):
        if z % e !=  0 and n-1 % e != 0:
            break;
            
    for d in range(1, z+1):
        if ((e*d)-1) % z ==  0:
            break;  
            
    for i in word:
        m = pow(ord(i),d)%n
        decrypt += chr(m)
    
    return decrypt

p = 11
q = 13
word = 'ENCRYPTION'
word2 = 'RASTAMAN'

print(word + " = " + encryption(p, q, word))
print(word2 + " = " + encryption(p, q, word2))

secret = encryption(p, q, word)
secret2 = encryption(p, q, word2)

print(secret + " = " + decryption(p, q, secret))
print(secret2 + " = " + decryption(p, q, secret2))