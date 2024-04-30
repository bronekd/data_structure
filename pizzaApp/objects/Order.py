
class Order:
    def __init__(self, address, meal):
        # todo adresa může být jako samostatný objekt
        self.__address = address
        self.__meal = meal



    def get_address(self):
        return self.__address

    def get_meal(self):
        return self.__meal

    def get_price(self):
        result = 0
        for m in self.__meal:
            result += m.get_price()

        return result

    def __str__(self):
        items = ""
        for m in self.__meal:
            items += f"  {m.get_name()}                 {m.get_price()} $"
        return f"""
        ************************************
                       Order
        ------------------------------------
        {items}
        ------------------------------------
        sum             {self.get_price()} $
        
        ************************************
        """
        #Vypsat objednávku
