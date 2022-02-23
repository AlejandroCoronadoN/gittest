import pandas as pd

def coro_fun(garnachas, tortas):
    """Returns the equivalent happines created by garnachas
    and tortas

    Args:
        garnachas (int): number of garnachas
        tortas (int): number of tortas
    """
    happytortas =  tortas * 1.67 #teorical number extracted from rayman series
    happygarnachas = garnachas * 1.33 #I have to admit this constant might be fake
    return  happytortas + happygarnachas