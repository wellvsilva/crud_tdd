from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'message': 'Testando Django com TDD',})

def pessoa_add(request):
    context = dict(form='form')
    return render(request, 'pessoa_detalhe.html', context)
