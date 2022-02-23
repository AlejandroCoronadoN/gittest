import pandas as pd

def another_fun():
    """Pritnts stuff
    """
    print('stuff')
    
    

    
    
def shared_fun(pizza:int, burgers:int):
    """A function that multiplies burgers and pizzas in order to obtain
    the area under the curve of your belly.

    Args:
        pizza (int): number of pizzas
        burgers (int): number of burguers
    """
    return pizza*burgers +2


def new_fun(diccionario:dict):
    """Iterates trough dictionary

    Args:
        diccionario (dict): any dictionary
    """
    for k in diccionario.key():
        print(k)
