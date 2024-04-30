
class Price:
    # nadefinovat magic metod pro matematické operace. sečíst 2 hodnoty s celými a desetinými čísly todo
    def __init__(self, integer, fraction):
        self.__integer = integer
        self.__fraction = fraction

    def get_price(self):
        return self.__integer + self.__fraction / 100

    def __str__(self):
        return f"{self.__integer},{self.__fraction}"

