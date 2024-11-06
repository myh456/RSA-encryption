def exgcd(a, b):
    # 扩展欧几里得算法，返回 (gcd, x, y) 使得 a * x + b * y = gcd
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = exgcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


def mod_inverse(e, phi_n):
    # 求 e 在模 φ(n) 下的逆元
    # 已知 ed ≡ 1 (mod φ(n)) 可以写作 ed - φ(n)k = 1
    gcd, d, k = exgcd(e, phi_n)
    # x 是 e 的逆元，但是它可能是负数，因此需要调整为正数
    return d % phi_n


class RSA:
    def __init__(self):
        self.sk = []

    # 生成公钥，保存私钥
    def subKey(self, p, q):
        n = p * q
        # 计算欧拉函数φ(n)
        phi_n = (p - 1) * (q - 1)
        # 选择与φ(n)互质的数e,这里选择了φ(n) - 1
        e = phi_n - 1
        # 计算e在φ(n)下的逆元
        d = mod_inverse(e, phi_n)
        self.sk = [e, n]
        return [d, n]

    # 加密函数
    def enc(self, plain):
        return (plain ** self.sk[0]) % self.sk[1]

    # 解密函数
    def dec(self, cipher, pk):
        return (cipher ** pk[0]) % pk[1]
