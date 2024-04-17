#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Seu principal objetivo é implementar a função `player`, que deve retornar uma lista de 4 cores, o seu próximo palpite.
Como exemplo, a função abaixo retorna um palpite aleatório.

Dicas:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
"""
from colors import *
from random import sample

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]


def player(guess_hist, res_hist):
    """
    Função principal do jogador.

    Esta função deve retornar o seu palpite, que deve ser uma lista de 4 cores.
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores

    Exemplo:
    return [RED, GREEN, BLUE, YELLOW]
    """
    if len(guess_hist) == 0:
        return [RED, GREEN, BLUE, YELLOW]
    else:
        return all_arrangements(4, [1, 2, 3, 4, 5, 6, 7], guess_hist, res_hist)

def all_arrangements(len_list, elements_list, guess_hist, res_hist):

    arrang = [0] * len_list

    def add_elements(elements, index):

        for i in elements:
            arrang[index] = i
            if index != len_list - 1:
                new_list_elements = list(set(elements) - {i}).copy()
                test = add_elements(new_list_elements, index=index + 1)
                if test is None:
                    continue
                else:
                    return test
            else:
                arrang_append = arrang.copy()
                if test_validation(arrang_append, guess_hist, res_hist):
                    test = num_in_color(arrang_append)
                    return test

    return add_elements(elements_list, 0)

def test_validation(test, guess_hist, res_hist):

    for previous_test in guess_hist:

        i = guess_hist.index(previous_test)

        previous_test = color_in_num(previous_test)

        if quantity_valid(test, previous_test, res_hist[i]) and position_valid(test, previous_test, res_hist[i]) and test != previous_test:
            continue
        else:
            return False
    
    return True



def quantity_valid(test, previous_test, res_test):
    diff = 4 - len(list(set(previous_test) - set(test)))
    return True if diff == res_test[0] else False

def position_valid(test, previous_test, res_test):
    qnt_positions = 0
    if test[0] == previous_test[0]: 
        qnt_positions +=1
    if test[1] == previous_test[1]: 
        qnt_positions +=1
    if test[2] == previous_test[2]: 
        qnt_positions +=1
    if test[3] == previous_test[3]: 
        qnt_positions +=1

    return True if qnt_positions == res_test[1] else False
    

def num_in_color(num_list):
    num_colors = {
        "1": RED,
        "2": GREEN,
        "3": BLUE,
        "4": YELLOW,
        "5": ORANGE,
        "6": BLACK,
        "7": WHITE
    }

    color_list = []

    for i in num_list:
        color_list.append(num_colors[str(i)])
    
    return color_list

def color_in_num(color_list):

    str_color_list = (color._text(i) for i in color_list)

    num_colors = {
        "Red": 1,
        "Green": 2,
        "Blue": 3,
        "Yellow": 4,
        "Orange": 5,
        "Black": 6,
        "White": 7
    }

    num_list = []

    for i in str_color_list:
        num_list.append(num_colors[i])

    return num_list
    