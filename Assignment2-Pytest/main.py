#Calci class just to implement addition,subtraction,multiplication and division of two numbers
class Calci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def product(self):
        return self.a * self.b

    def division(self):
        try:
         return self.a / self.b
        except ZeroDivisionError:
            return 'Can\'t divide with zero'