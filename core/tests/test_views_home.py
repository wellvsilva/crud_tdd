# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase
#from selenium import webdriver

from django.test import Client

class ViewHomeTest(TestCase):

    # Crio uma instancia do objeto response pra ser compartilhado por todos os testes
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('home'), {})

    def tearDown(self):
        pass

    # testar o status_code da requisição    
    def test_request_return_code_200(self):
        'deve retornar status_code 200'
        self.assertEqual(self.response.status_code, 200)

    # testar o html retornado pela requisoção
    def test_template_used(self):
        'deve estar usando o template index.html'
        self.assertTemplateUsed(self.response, 'index.html')

    # testar principais tags HTML
    def test_principals_tags_html(self):
        'deve conter as principais tags HTML: <h1>, <form>'
        self.assertIn('<h1>', self.response.content, 'html deve ter a tag <h1>')
        self.assertIn('<h3>', self.response.content, 'html deve ter a tag <h3>')
        self.assertContains(response=self.response, text='<a', count=1, msg_prefix='deve contexr 1 tag de link <a')

    # testar os dados no HTML
    def test_deve_conter_dados_no_contexto(self):
        'Deve conter dados no contexto'
        self.assertIn('Django TDD', self.response.content)
        self.assertIn('Testando Django com TDD', self.response.content)
        self.assertIn('Pessoas', self.response.content)
        self.assertContains(self.response, 'href="%s"' % reverse('pessoa_list'), 1)
        
    # testar as variaveis no contexto
    def test_deve_variaveis_no_contexto(self):
        'deve conter variaveis no contexto'		
        self.assertTrue('user' in self.response.context)
        self.assertTrue('message' in self.response.context)
   