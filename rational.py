from math import copysign


def gcd(a, b):
    """Computes greatest common divisor of two values"""
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational:
    """Representation of rational number
    >>> Rational(1,2)
    1/2
    >>> Rational(2,4)
    1/2
    >>> Rational(1,2) + Rational(3,4)
    5/4
    >>> Rational(-1,2)
    -1/2
    >>> Rational(5)
    5
    >>> float(Rational(3,4))
    0.75
    """

    def __init__(self, top=1, bottom=1):
        """Initializes Rational instance"""

        # do not allow 0 d
        if bottom == 0:
            raise ZeroDivisionError("Cannot have 0 d")

        # assign attribute values
        gcdnum = gcd(top, bottom)
        self.n = int(abs(top/gcdnum))
        self.d = int(abs(bottom/gcdnum))
        self.sign = copysign(1, top * bottom)


    def __add__(self, other):
        n = self.sign*self.n * other.d + other.sign*other.n * self.d
        d = self.d * other.d
        return Rational(n,d)

    def __sub__(self, other):
        n = other.sign*self.n * other.d - self.sign*other.n * self.d
        d =self.sign*other.sign*self.d * other.d
        return Rational(n,d)

    def __mul__(self, other):
        n = self.sign*other.sign*self.n * other.n
        d = self.d * other.d
        return Rational(n,d)

    def __truediv__(self, other):
        n = self.sign*self.n * other.d
        d =other.sign* self.d * other.n
        return Rational(n,d)

    def __str__(self):
        if self.sign < 0:
            return "-{}/{}".format(self.n, self.d)
        return "{}/{}".format(self.n, self.d)

    __repr__ = __str__

    def __float__(self):
        pass


if __name__ == '__main__':
    import doctest

    # doctest.testmod()
    x = Rational(1, -4)
    y = Rational(1, 3)
    print(x)
    print(x + y)
    print(x*y)
    print(x/y)

