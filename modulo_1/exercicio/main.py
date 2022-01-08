from numero_natural import *
from divisivel import *
# from pede_numero import *

def main(x):
    if multiplo_5_7(x):
        return 'fizzbuzz'

    elif multiplo_5(x):
        return 'fizz'  

    elif multiplo_7(x):
        return 'buzz' 

    else:
        return 'miss' 


if __name__ == '__main__':

    while True:
        try:
            x = float(input('digite um numero natural: '))
            if natural(x):
                break
        except:
            print('os dados que você inseriu é invalido')
    print(main(x))
