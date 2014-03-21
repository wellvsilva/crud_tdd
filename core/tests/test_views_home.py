# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from django.test import Client

class ViewHomeTest(TestCase):

    # Crio uma instancia do objeto response pra ser compartilhado por todos os testes
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('home'), {})

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
        self.assertContains(self.response, '<h1')
        self.assertContains(self.response, '<h3')

    # testar os dados no HTML
    def test_deve_conter_dados_no_contexto(self):
        'Deve conter dados no contexto'
        self.assertContains(self.response, 'Django TDD')
        self.assertContains(self.response, 'Testando Django com TDD')
        
    # testar as variaveis no contexto
    def test_deve_variaveis_no_contexto(self):
        'deve conter variaveis no contexto'		
        self.assertTrue('user' in self.response.context)
        self.assertTrue('message' in self.response.context)
   