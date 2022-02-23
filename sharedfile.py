import pandas as pd

def another_fun():
    """Pritnts stuff
    """
    print('stuff')
    
    
def shared_fun_toto(teni:int):
    """Calculates the numeber of kiloemters you can run given the 
    number of teni in your stock

    Args:
        teni (int): Number of teni
    """
    if teni ==1:
        #Come on man, who runs with a single teni! thats why is called tenis
        return 0 
    else:
        return teni*1000
    
    
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
