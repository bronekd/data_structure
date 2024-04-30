from objects import *

p = Price(10,50)
t = Topping("chess", p)

print(p)
print(t)


#vytvoření seznamu příloh toppings a pizz
pizza = Pizza("TEST_PIZZA", [t])

# zapsat testovací topping a do json file



