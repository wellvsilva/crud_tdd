# coding: utf-8
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from core.forms import PessoaForm
from core.models import Pessoa


class ViewPessoaAddTest(TestCase):

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
        self.assertTrue(self.resp.content.startswith('<!DOCTYPE html>'))
        self.assertIn('<h1>', self.resp.content)
        self.assertIn('<form', self.resp.content)
        self.assertIn('method="POST"', self.resp.content)
        self.assertIn('action="%s"' % reverse('pessoa_save', kwargs={'pk': 0}), self.resp.content)
        self.assertContains(self.resp, '<input', 4)
        self.assertContains(self.resp, "<input type='hidden' name='csrfmiddlewaretoken'", 1)
        self.assertContains(self.resp, '<input id="id_nome"', 1)
        self.assertContains(self.resp, '<input id="id_cpf"', 1)
        self.assertContains(self.resp, "<input type='submit'", 1)
        self.assertContains(self.resp, ">Cancelar</a>", 1)
        self.assertContains(self.resp, 'href="%s"' % reverse('home'), 1)
        self.assertTrue(self.resp.content.endswith(b'</html>'))

    def test_html_deve_conter_dados(self):
        'deve conter dados esperado no html'
        self.assertIn('Cadastro de Pessoa', self.resp.content)
        self.assertIn('csrfmiddlewaretoken', self.resp.content)

    def test_contexto_deve_conter_variaveis(self):
        self.assertTrue('form' in self.resp.context, 'deve conter no contexto a variavel form')
        self.assertTrue('csrf_token' in self.resp.context, 'deve conter no contexto a variavel csrf_token')

    def test_tipos_variaveis_contexto(self):
        form  = self.resp.context['form']
        self.assertIsInstance(form, PessoaForm, 'form deve ser uma instancia do tipo PessoaForm')   

class ViewPessoaSaveTest(TestCase):
    def setUp(self):
        pass

    def test_deve_conter_2_campos(self):
        'o form deve conter 2 compos'
        form = PessoaForm()
        self.assertItemsEqual(['nome', 'cpf'], form.fields)

    def test_erro_cpf_sem_dados(self):
        'cpf deve conter valor, campo obrigatorio'
        data = dict(nome='Fabiano', cpf='')
        form = PessoaForm(data)
        form.is_valid()
        self.assertItemsEqual(['cpf'], form.errors)

    def test_erro_nome_sem_dados(self):
        'nome deve conter valor, campo obrigatorio'
        data = dict(nome='', cpf='123')
        form = PessoaForm(data)
        form.is_valid()
        self.assertItemsEqual(['nome'], form.errors)

    def test_send_form_post_not_save(self):
        'não deve salvar quando os dados estão invalidos'
        data = dict(nome='Fabiano', cpf='')
        resp = self.client.post(reverse('pessoa_save', kwargs={'pk': 0}), data)
        self.assertEquals(resp.status_code, 200)
        form = resp.context['form']
        self.assertItemsEqual(['cpf'], form.errors)

    def test_send_form_post_update(self):
        'deve atualizar os dados da Pessoa'
        p = Pessoa.objects.create(nome='Fabiano', cpf='123')
        new_data = dict(id=p.id, nome='Fabiano', cpf='123456')
        resp = self.client.post(reverse('pessoa_save', kwargs={'pk': p.pk}), new_data)
        self.assertEqual(resp.status_code, 302, 'Deve ter retornado status_code 302 se atualizou com sucesso')
        np = Pessoa.objects.get(cpf='123456')
        self.assertIsNotNone(np, 'Deve ter retornado um objeto Pessoa')


class ViewPessoaDeleteTest(TestCase):
    def setUp(self):
        pass

    def test_delete_sucess(self):
        'deve deletar o registro com sucesso'
        p = Pessoa.objects.create(nome='Fabiano', cpf='123')
        resp = self.client.get(reverse('pessoa_delete', kwargs={'pk': p.id}))
        self.assertEqual(resp.status_code, 302, 'deve retornar status_code 302 ao encontrar a url')
        self.assertFalse(Pessoa.objects.exists(), 'Não pode existir o registro após executar o delete')
        self.assertRedirects(response=resp, expected_url=reverse('home'), msg_prefix='Deve ser redirecionado para home ao deletar')
