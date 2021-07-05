def sha1(data):
    bytes = ""

    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0

    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits


    while len(pBits)%512 != 448:
        pBits+="0"
   
    pBits+='{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]


    def rol(n, a):
        return ((n << a) | (n >> (32 - a))) & 0xffffffff

    for c in chunks(pBits, 512): 
        words = chunks(c, 32)
        w = [0]*80

        for n in range(0, 16):
            w[n] = int(words[n], 2)

        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a = A
        b = B
        c = C
        d = D
        e = E

        for t in range(0, 80):

            if 0 <= t <= 19:
                Ft = (b & c) | ((~b) & d)
                Kt = 0x5A827999
            elif 20 <= t <= 39:
                Ft = b ^ c ^ d
                Kt = 0x6ED9EBA1
            elif 40 <= t <= 59:
                Ft = (b & c) | (b & d) | (c & d) 
                Kt = 0x8F1BBCDC
            elif 60 <= t <= 79:
                Ft = b ^ c ^ d
                Kt = 0xCA62C1D6

            temp = rol(a, 5) + Ft + e + Kt + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp


        A = A + a & 0xffffffff
        B = B + b & 0xffffffff
        C = C + c & 0xffffffff
        D = D + d & 0xffffffff
        E = E + e & 0xffffffff
    return '%08x%08x%08x%08x%08x' % (A, B, C, D, E)
