# pohled vypis menu asi menu
import json

def print_main_menu():
    print("""
    ----------------MAIN MENU ---------------
    [1] - Nová objednávka
    [2] - Zjistit stav objednávky
    [3] - Vybavit poslední objednávku
    [0] - Ukončit aplikaci
    """)


def print_pizza_menu():
    x = open("resources/pizza_list.json","r")
    data = json.load(x)

    print(f"""
    Seznam Pizz:
    {data}
    """)

def print_bye():
    print("Naschledanou a dekuji za použiti aplikace")

def input_address():
    address = input("Zadej adresu pro doruceni: ")
    return address


def create_order_message(order):
    print("Objednavka vytvorena")
    print("info o objednavce")

def wrong_choice_message():
    print("Zadal jsi zlou volbu!! ")





