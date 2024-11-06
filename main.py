from rsa import RSA

if __name__ == '__main__':
    rsa = RSA()
    pk = rsa.subKey(211, 149)
    c = rsa.enc(156)
    print('密文:', c)
    print('明文:', rsa.dec(c, pk))
