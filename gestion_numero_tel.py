#!/usr/local/bin/python3
#--*--coding:utf8--*-- 

def print_numbers(numbers):
    print("Numéro de Téléphone:")
    for k, v in numbers.items():
        print("Nom:", k, "\tNuméro:", v)
    print()
 
def add_number(numbers, name, number):
    numbers[name] = number
 
def lookup_number(numbers, name):
    if name in numbers:
        return "Le nombre est " + numbers[name]
    else:
        return name + " n'a pas été trouvé"
 
def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," non trouvé")
 
def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()
 
def save_numbers(numbers, filename):
    out_file = open(filename, "wt")
    for k, v in numbers.items():
        out_file.write(k + "," + v + "\n")
    out_file.close()
 
def print_menu():
    print('1. Afficher les numéros de téléphone')
    print('2. Ajouter un numéro de téléphone')
    print('3. Enlever un numéro de téléphone')
    print('4. Chercher un numéro de téléphone')
    print('5. Charger un numéro')
    print('6. Sauvegarder un numéro')
    print('7. Quitter')
    print()
 
phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Ajouter un nom et un numéro")
        name = input("Name: ")
        phone = input("Numéro: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("enlever le nom et le numéro")
        name = input("Nom: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Chercher un numéro")
        name = input("Nom: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = input("Fichier à charger: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = input("Fichier à sauvegarder: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()
 
print("Au revoir")
