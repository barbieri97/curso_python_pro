import pytest
from numero_natural import positivo, inteiro, natural
from divisivel import multiplo_5, multiplo_7, multiplo_5_7
from main import main

class TesteNatural():
    @pytest.mark.parametrize('entrada, saida', [
        (-1, False),
        (1, True),
        (0, True),
        (5.2, True),
        (-5.2, False)])
    def teste_negativo(self, entrada, saida):
        assert positivo(entrada) == saida
    
    @pytest.mark.parametrize('entrada, saida', [
        (25, True),
        (0, True),
        (-5, True),
        (45.5, False),
        (-5.7, False)])
    def teste_inteiro(self, entrada, saida):
        assert inteiro(entrada) == saida

    @pytest.mark.parametrize('entrada, saida', [
        (5, True),
        (-5, False),
        (5.5, False),
        (-5.5, False),
        (0, True)])
    def teste_natural(self, entrada, saida):
        assert natural(entrada) == saida

class TesteDivisivel():
    @pytest.mark.parametrize('entrada, saida', [
        (5, True),
        (15, True),
        (83547609345, True),
        (7,False),
        (19, False)
    ])
    def teste_divisivel_5(self, entrada, saida):
        assert multiplo_5(entrada) == saida

    @pytest.mark.parametrize('entrada, saida', [
        (7, True),
        (21, True),
        (147, True),
        (5,False),
        (3, False)
    ])
    def teste_divisivel_7(self, entrada, saida):
        assert multiplo_7(entrada) == saida

    @pytest.mark.parametrize('entrada, saida', [
        (70, True),
        (21, False),
        (140, True),
        (5,False),
        (3, False)
    ])
    def teste_divisivel_5_7(self, entrada, saida):
        assert multiplo_5_7(entrada) == saida

# class TesteColetaNumero():
#     @pytest.mark.parametrize('entrada, saida', [
#         ('andre', False),
#         ('6', 6),
#         (7, 7)
#     ])
#     def teste_numero(self, entrada, saida):
#         assert numero() == saida

class TesteMain():
    @pytest.mark.parametrize('entrada, saida', [
        (15, 'fizz'),
        (21, 'buzz'),
        (0, 'fizzbuzz'),
        (3, 'miss'),
        (140, 'fizzbuzz')
    ])
    def teste_main(self, entrada, saida):
        assert main(entrada) == saida 