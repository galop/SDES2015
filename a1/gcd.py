def gcd(a, b):
    ''' returns gcd (greatest common divisor)
    args: a, b positive integers (a,b >= 0)
    '''    
    if type(a) not in (int, long) or type(b) not in (int, long):
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError
    def gcdHelper(a, b):
        ''' Recursive method for gcd, Euler's method'''
        if b == 0:
            return a
        elif a == 0:
            return b
        else:
            return gcdHelper(b, a % b)
    return gcdHelper(a, b)

def main():
    pass
    
if __name__ == "__main__":
    main()
