
from objects import *
import json

p = Price(10,50)
t = Topping("chess", 10)

#print(p)
print(t)


#vytvoření seznamu příloh toppings a pizz

pizza = Pizza("TEST_PIZZA", [t])
with open("test.json", "w") as file:
    json.dump(pizza.to_dict(), file)





