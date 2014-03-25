# coding: utf-8
from django.test import TestCase
from core.models import Pessoa

class ModelPessoaTest(TestCase):
    def setUp(self):
        pass

    def test_unicode(self):
        'a instancia de Pessoa deve retornar o unicode de nome'
        nome = 'Fabiano'
        p = Pessoa.objects.create(nome=nome, cpf='123')
        self.assertEqual(str(p), nome)

    def test_create_pessoa(self):
        'deve criar uma pessoa e ter uma pk'
        p = Pessoa.objects.create(nome='Fabiano', cpf='123')
        self.assertTrue(p.pk > 0)
