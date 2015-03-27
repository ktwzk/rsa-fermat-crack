import string

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=False):
    a = isqrt(n) 
    b2 = a**2 - n
    b = isqrt(n)
    count = 0
    while b**2 != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a**2 - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def crack(n, e, c, output_type='str'):
    p, q = fermat(n)
    phi = (p-1) * (q-1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    if output_type=='int':
        return m
    elif output_type=='str':
        m = str(hex(m))[2:-1].decode("hex")
        return m
    elif output_type='hex':
        m = str(hex(m))[2:-1]
        return m



#Edit it, if you want
n,e,c = map(int, raw_input('n e c').split())
print crack(n,e,c)
