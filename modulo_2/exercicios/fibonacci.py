class Fibonacci():
    def __init__(self, var):
        self.anterior = 0
        self.proximo = 1
        self.iteracao = var
    
    def __iter__(self):
        self.i = 0

        return self
    
    def __next__(self):
        self.i += 1

        if self.i == 1 and self.iteracao != 0:
            self.iteracao -= 1
            return 0
        if self.i == 2 and self.iteracao != 0:
            self.iteracao -= 1
            return 1
        elif self.iteracao == 0:
            raise StopIteration
        else:
            x = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = x
            self.iteracao -= 1
            return self.proximo

