import pytest
from fibonacci import Fibonacci

class TestarFuncFibonacci:
    @pytest.mark.parametrize('entrada,saida', [
        (1, {0 : 0}),
        (3, {0 : 0, 1 : 1, 2 : 1}),
        (5, {0 : 0, 1 : 1, 2 : 1, 3 : 2, 4 : 3}),
        (10, {0 : 0, 1 : 1, 2 : 1, 3 : 2, 4 : 3, 5 : 5, 6 : 8, 7 : 13, 8 : 21, 9 : 34})
        ])
    def test_fibonnacci(self, entrada, saida):
        cont = Fibonacci(entrada)
        x = iter(cont)
        s = {k : v for k,v in enumerate(x)}
        assert s == saida