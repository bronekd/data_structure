from .Price import Price
class Pizza:
    def __init__(self, name, toppings):
        #todo přidat druh těsta (tenky, tlusty), přidat druh základu (rajče, smetana)
        # Možnost přidat extra Topping
        self.name = name
        self.__toppings = toppings
        self.__DOUGHT_PRICE = Price(5, 90)  # cena těsta jako konstanta

    def get_name(self):
        return self.name

    def get_price(self):
        result = self.__DOUGHT_PRICE.get_price()
        for i in self.__toppings:
            result += t.get_price().get_price()  # první get price cena a pak to druhé vrací tu samotnou hodnotu

        return result

    def __str__(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ", "
        #odstraneni posledni čarky

        return f"""
{self.name}                  {self.get_price()} $
-----------------------------------------------
{topps}
"""


