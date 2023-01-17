class Price:
    def __init__(self, value):
        self.value = round(float(value), 2)

    def __str__(self):
        return f"{self.value}zł"

    @classmethod
    def from_usd(cls, usd):
        return cls(float(usd) * 3.80)

    @classmethod
    def from_eur(cls, eur):
        return cls(float(eur) * 4.50)