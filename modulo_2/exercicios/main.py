from fibonacci import Fibonacci
from time import sleep


if __name__ == '__main__':
    while True:
        try:
            i = int(input('digite o numero elementos da sequencia fibonacci que deseja: '))
            cont = Fibonacci(i)
            x = iter(cont)
            print({k : v for k,v in enumerate(x)})
            break
        except:
            print('o valor que inseriu não é valido, entre um valor inteiro.')
            sleep(2)
            print('reiniciando o programa...')
            sleep(3)

