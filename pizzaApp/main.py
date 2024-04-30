# hlavní soubor pizza

from views import *
from objects import Order, Queue
from pizzaAppFunkcionality import create_new_order

def run_app():
    # TODO zálohování a načtení z paměti
    orders_queue = ()

    while True:
        print_main_menu()
        # TODO ošetřit o kontrolu vstupu
        user_choice = int(input("Zadej volbu: "))

        if user_choice == 1:
            create_new_order(orders_queue)

        elif user_choice == 2:
            pass

        elif user_choice == 3:
            pass
        elif user_choice == 4:
            print(orders_queue.show())

        elif user_choice == 0:
            # TODO uložení orders do paměti pomocí pickle
            print_bye()
            exit()

        else:
            wrong_choice_message()


run_app()






