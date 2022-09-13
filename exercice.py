#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0
    # Expression renvoie déjà un booléen; pas besoin d'un if-else.


def remove_third_char(string: str) -> str:
    # Exercice vraiment chouette selon le professeur.
    return string[0:2]+string[3:]
    # String est immuable. On doit donc créer une nouvelle string. On fait donc une tranche.


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for letter in string:
        if letter == old_char:
            new_string += new_char
        else:
            new_string += letter
    return new_string


def get_number_of_char(string: str, char: str) -> int:
    count = 0
    for letter in string:
        if letter == char:
            count += 1
    return count


def get_number_of_words(sentence: str, word: str) -> int:
    count = 0
    for letter in sentence:
        if letter not in word:
            pass
        else:
            count += 1
    count /= len(word)
    return int(count)



def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractères dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractères dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
