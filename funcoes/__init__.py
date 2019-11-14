import requests
import sqlite3

pathdb = 'db/users'

def verificacao_site(link):
    try:
        a = requests.get(link)
    except Exception:
        return False
    else:
        return True


def criar_shorturl(link,site):

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

    for i in cursor.fetchall():
        a=i[0]+1

    # Criando a url com o último valor da sequência +1
    a = conversor(a)

    # Fechando banco de dados
    conn.close()

    return site +'/'+a

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


def post(shortUrl,user,link_original):
    # cadastra uma nova URL no sistema
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO cadastro (hits,nome,shortUrl,url)
    VALUES (?,?,?,?)
    """, (int(0), str(user),str(shortUrl),str(link_original)))
    conn.commit()
    conn.close()


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
