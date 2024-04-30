

from views import (print_pizza_menu,
                   create_order_message)
from objects import Order


def create_new_order(orders_queue):
    print_pizza_menu()
    user_pizza = input("Zadej volbu: ")
    user_address = input("Zadej adresu: ")
    user_order = Order(address=user_address, meal=[])
    #orders_queue.enqueue(user_order)  # opravit
    orders_queue.enqueue(user_order)
    create_order_message(user_order)


