from views import (print_pizza_menu,
                   create_order_message )
from objects import Order
def create_new_order(orders_queue):
    print_pizza_menu()
    user_pizza = int(input("Zadej volbu: "))
    user_adress = input("Zadej adresu: ")
    user_order = Order(address=user_adress, meal=[])
    orders_queue.enqueue(user_order)  # opravit
    create_order_message(user_order)