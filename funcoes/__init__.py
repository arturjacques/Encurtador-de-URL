import requests
import sqlite3


def verificacao_site(link):
    try:
        a = requests.get(link)
    except Exception:
        return False
    else:
        return True


def criar_shorturl(link):
    pathdb = 'db/users'

    # Conectando ao banco de dados
    conn = sqlite3.connect(pathdb)

    # Definindo cursor
    cursor = conn.cursor()

    # Achando o último valor
    cursor.execute(f"""
    SELECT seq 
    FROM sqlite_sequence 
    Order BY seq asc
    LIMIT 1;
    """)

    if cursor.fetchall() != []:
        a = cursor.fetchall()[0] + 1
    elif cursor.fetchall() == []:
        a = 0

    a = conversor(a)

    # Criando a url com o último valor da sequência +1

    # Fechando banco de dados
    conn.close()


def conversor(a):
    numeros = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(numeros)

    convertido = ''

    while a > base:
        resto = a % base
        convertido = numeros[resto] + convertido
        a = int(a / base)

    convertido = numeros[a] + convertido

    return convertido


def post(link):
    # cadastra uma nova URL no sistema
    pass


def stats():
    # retorna estatisticas globais do sistema
    pass


def users_stats(userid):
    # retorna as estatisticas das URLS de um usuário
    pass


def stats_url(urlID):
    # retorna as estatisticas de uma URL específica
    pass


def delete_url(urlID):
    # deleta URL do sistema
    pass


def create_user(usuario):
    # cria um novo usuário
    pass
