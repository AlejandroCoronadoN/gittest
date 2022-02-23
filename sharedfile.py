import pandas as pd

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
        return teni*100