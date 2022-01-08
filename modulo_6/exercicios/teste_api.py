import pytest
from requests import get, post
from json import loads


class TestAPI():
    def setup(self):
        self.url = 'http://127.0.0.1:8000/'

    def test_status(self):
        resp = get(self.url)
        assert resp.ok

    def test_get_method (self):
        resp = get(self.url)
        conteudo = loads(resp.text)
        assert conteudo['message'] == 'Tudo ok'
    
    
    @pytest.mark.parametrize('entrada, saida', [
        ({'var1' : 1, 'var2' : 1, 'operacao' : 'adicao' }, '2'),
        ({'var1' : 1, 'var2' : 1, 'operacao' : 'subtracao'}, '0'),
        ({'var1' : 10, 'var2' : 5, 'operacao' : 'divisao'}, '2.0'),
        ({'var1' : 2, 'var2' : 2, 'operacao' : 'multiplicacao'}, '4')
    ])
    def test_post_method(self, entrada, saida):
        resp = post(self.url + 'calculadora/', json=entrada)
        assert resp.text == saida