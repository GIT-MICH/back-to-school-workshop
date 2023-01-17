class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return round(a / b, 2)
        except ZeroDivisionError:
            return 'Do not divide by 0!.'


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add(self, a, b):
        add = super().add(a, b)
        self.history.append(f"{a} + {b} = {add}")
        return add

    def sub(self, a, b):
        subtract = super().sub(a, b)
        self.history.append(f"{a} - {b} = {subtract}")
        return subtract

    def mul(self, a, b):
        multiply = super().mul(a, b)
        self.history.append(f"{a} * {b} = {multiply}")
        return multiply

    def div(self, a, b):
        divided = super().div(a, b)
        self.history.append(f"{a} / {b} = {divided}")
        return divided


# c1 = Calculator()
# print(c1.add(5, 3))
c2 = LoggingCalculator()
print(c2.add(6, 4))
print(c2.add(6, 6))
print(c2.div(50, 0))
print(c2.mul(8, 6))
print(c2.history)
