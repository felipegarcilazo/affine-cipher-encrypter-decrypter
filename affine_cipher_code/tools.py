import math

def euclidean(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        quotients.append(math.floor(x/y))
        x, y = y, x-math.floor(x/y)*y
    while quotients:
        x, y = y, x-quotients[-1]*y
        quotients.pop()
    return y

def encrypt(alphabet, m_key, a_key, unencrypted_txt):
    encrypt_txt = ''
    for i in range(0, len(unencrypted_txt)-1):
        encrypt_txt += alphabet[((alphabet.index(unencrypted_txt[i]) * int(m_key)) + int(a_key)) % len(alphabet)]
    return encrypt_txt

def decrypt(alphabet, m_key, a_key, encrypt_txt):
    unencrypt_txt = ''
    m_key_inverse = euclidean(len(alphabet), int(m_key)) % len(alphabet)
    for i in range(0, len(encrypt_txt)-1):
        unencrypt_txt += alphabet[int(((alphabet.index(encrypt_txt[i]) - int(a_key)) * m_key_inverse) % len(alphabet))]
    return unencrypt_txt
