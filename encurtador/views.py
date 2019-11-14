from django.shortcuts import render
from funcoes import verificacao_site
from funcoes import criar_shorturl
from funcoes import post
from django.contrib.sites.models import Site

# Create your views here.
def criar_link_view(request):
    #inicializando variável
    a=False
    host=request.get_host()
    #variável responsável pelas informações da tela
    context={}
    #verificação se o site existe
    if request.method == "POST":
        link=request.POST.get('url')
        a = verificacao_site(link)
        if a==False and link[:4]!=('http'):
            linki='http://'+link
            a = verificacao_site(linki)
            if not a:
                linki = linki.replace('http','https')
                a =verificacao_site(linki)
        if a:
            context['msg1']=f"página {link} encontrada"
        else:
            context['msg1']=f'Erro 404 página {link} não encontrada'

    #verificação se o site já foi cadastrado no banco de dados pelo usuário
    if a:
        pass
    #Criar nova URL
    if a:
        shorturl=criar_shorturl(linki,request.get_host())
    #Cadastrar no banco de dados
        post(shorturl,request.user,linki)

    return render(request, "entrada.html", context)
