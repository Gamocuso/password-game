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
        return all_arrangements(4, colors, guess_hist, res_hist)

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
                if test_validation(arrang, guess_hist, res_hist):
                    return arrang
                    

    return add_elements(elements_list, 0)

def test_validation(test, guess_hist, res_hist):

    for i in range(len(guess_hist)):

        if quantity_valid(test, guess_hist[i], res_hist[i]) and position_valid(test, guess_hist[i], res_hist[i]) and test != guess_hist[i]:
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
    
