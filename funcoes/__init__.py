import requests

def encurtar(user,link):
    try:
        a = requests.get(link)
    except Exception:
        return 'Erro 404 Página não encontrada'
    else:
        return 'página encontrada'

def post(link):
    #cadastra uma nova URL no sistema
    pass

def stats():
    #retorna estatisticas globais do sistema
    pass

def users_stats(userid):
    #retorna as estatisticas das URLS de um usuário
    pass

def stats_url(urlID):
    #retorna as estatisticas de uma URL específica
    pass

def delete_url(urlID):
    #deleta URL do sistema
    pass

def create_user(usuario):
    #cria um novo usuário
    pass