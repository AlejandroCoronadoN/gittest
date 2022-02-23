import pandas as pd 

def toto_fun(tacos:int, tlayudas:int):
    """Calculate happiness based on the numbe rof tlayudas and
    tacos that you eat on a friday night.

    Args:
        tacos (int): number of tacos
        tlayudas (int): numbe rof tlayudas
    """
    happines_tacos = tacos *1.2
    happines_tlayudas = tlayudas * 1.999
    return happines_tacos + happines_tlayudas