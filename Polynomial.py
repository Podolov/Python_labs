import operator

class Polynomial:
    def __init__(self, coefss):
        if not coefss:
            self.coeffs = [0]
            self.degree = 0
            return

        for i, coeff in enumerate(coefss):
            if not isinstance(coeff, (int, float)):
                raise TypeError("polynomial coeffs should have int or float types!")

        self.coeffs = []
        self.coeffs[0:len(coefss)] = coefss[:]

        i = 0
        while ((i < len(self.coeffs)) and (self.coeffs[i] == 0)):
            self.coeffs.pop(0)
        if not self.coeffs:
            self.coeffs.insert(0, 0)

        self.degree = len(self.coeffs) - 1

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if (self.degree == other.degree):
                result = list(map(operator.add, self.coeffs, other.coeffs))
                return Polynomial(result)
            elif (self.degree > other.degree):
                rhPolynomialCoeffs = [0] * (self.degree - other.degree) + other.coeffs
                result = list(map(operator.add, self.coeffs, rhPolynomialCoeffs))
                return Polynomial(result)
            else:
                lhPolynomialCoeffs = [0] * (other.degree - self.degree) + self.coeffs
                result = list(map(operator.add, lhPolynomialCoeffs, other.coeffs))
                return Polynomial(result)
        else:
            if not isinstance(other, (int, float)):
                raise TypeError("incorrect type of value!")
            result = Polynomial(self.coeffs)
            result.coeffs[len(result.coeffs) - 1] += other
            return result

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (self.degree + other.degree + 1)
            for i, l in enumerate(self.coeffs):
                for j, r in enumerate(other.coeffs):
                    result[i + j] += l * r
            return Polynomial(result)
        else:
            if not isinstance(other, (int, float)):
                raise TypeError("incorrect type of value!")
            result = Polynomial([coef * other for coef in self.coeffs])
            return result

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("incorrect type of value!")
        return self.coeffs == other.coeffs

    def __str__(self):
        result = ""
        count = len(self.coeffs)
        if (count == 1):
            result += str(self.coeffs[0])
            return result
        for i, coeff in enumerate(self.coeffs):
            if ((count - 1 - i) == self.degree):
                if (self.degree == 1):
                    dgr = ''
                else:
                    dgr = str((self.degree))
                if (coeff == -1):
                    symb = '-'
                elif (coeff == 1):
                    symb = ''
                else:
                    symb = str(coeff)
                result = result + symb + 'x' + dgr
            elif ((count - 1 - i) == 0):
                if (coeff > 0):
                    result += '+' + str(coeff)
                elif (coeff < 0):
                    result += str(coeff)
                return result
            else:
                if (coeff != 0):
                    if (self.degree - i == 1):
                        dgr = ''
                    else:
                        dgr = str((self.degree - i))
                if (coeff == -1):
                    symb = '-'
                elif (coeff == 1):
                     symb = ''
                else:
                    symb = str(coeff)
                if (coeff > 0):
                    result = result + '+' + symb + 'x' + dgr
                else:
                    result = result + symb + 'x' + dgr