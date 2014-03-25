from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from core.forms import PessoaForm
from core.models import Pessoa


def home(request):
    return render(request, 'index.html', {'message': 'Testando Django com TDD',})

def pessoa_add(request):
    context = {'form': PessoaForm(), 'pk': 0}
    return render(request, 'pessoa_detalhe.html', context)

def pessoa_save(request, pk=0):
    form = PessoaForm(request.POST)
    if not form.is_valid():
        return render(request, 'pessoa_detalhe.html', {'form': form, 'pk': pk})

    if int(pk) > 0:
        return update(request, form, pk)

    return create(request, form)


def create(request, form):
    form.save()
    return HttpResponseRedirect(reverse('home'))


def update(request, form, pk):
    p = form.save(commit=False)
    p.id = pk
    p.save()
    return HttpResponseRedirect(reverse('home'))


def pessoa_delete(request, pk):
    p = get_object_or_404(Pessoa, pk=pk)
    p.delete()
    return HttpResponseRedirect(reverse('home'))


