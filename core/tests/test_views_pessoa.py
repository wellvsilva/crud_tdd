# coding: utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class ViewPessoaCadastroTest(TestCase):

    def setUp(self):
        c = Client()
        self.data = dict(nome='Fabiano', cpf='123456789')
        self.resp = c.post(reverse('pessoa_add'), self.data)

    # testar se o retorno do request é o esperado [status_code = 200]
    def test_status_code_request(self):
        'deve retornar status_code 200 no request'
        self.assertEquals(self.resp.status_code, 200)

    # testar se está usando o template esperado [pessoa_detalhe.html]
    def test_deve_estar_usando_template_pessoa_detalhe(self):
        'deve estar usando o template pessoa_detalhe.html'
        self.assertTemplateUsed(self.resp, 'pessoa_detalhe.html')

    # testar se o html contem as principais tags esperada
    def  test_deve_conter_principais_tags_html(self):
        'deve conter as principais tags HTML: <h1>, <form>'
        self.assertContains(self.resp, '<h1')
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)

    def test_html_deve_conter_dados(self):
        'deve conter dados esperado no html'
        self.assertContains(self.resp, 'Cadastro de Pessoa')
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_contexto_deve_conter_variaveis(self):
        self.assertTrue('form' in self.resp.context, 'deve conter no contexto a variavel form')
        self.assertTrue('csrf_token' in self.resp.context, 'deve conter no contexto a variavel csrf_token')

