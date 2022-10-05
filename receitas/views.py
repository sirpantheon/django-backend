from django.shortcuts import render

receitas = {
    1:  'Lasanha',
    2: 'Sorvete',
    3: 'Sopa',
    4: 'Bola de Chocolate'
}

dados ={
    'nome_das_receitas' : receitas
}

def index(request):
    return render(request, 'index.html',dados)


def receita(request):
    return render(request, 'receita.html')