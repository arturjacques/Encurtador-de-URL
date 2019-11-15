import requests
import sqlite3
import json

pathdb = 'db/users'

def verificacao_site(link):
    try:
        a = requests.get(link)
    except Exception:
        return False
    else:
        return True


def criar_shorturl(host):
    """
    Essa função recebe o host do site e é capaz de criar um URL único.
    Para que não haja conflito entre as URLS criadas por essa função e URLS do site
    todas as URLS destinadas ao controle do site devem conter um ponto final
    uma vez que esse código pode escrever qualquer combinação de números e letras.
    Porém não utiliza caracteres especiais.

    """


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
    a=0
    for i in cursor.fetchall():
        a=i[0]+1

    # Criando a url com o último valor da sequência +1
    a = conversor(a)

    # Fechando banco de dados
    conn.close()

    return host +'/'+a

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


def post(shortUrl,request,link_original):
    #criar função para redirecionar
    criar_funcao(shortUrl,link_original,request.get_host())
    #cadastra uma nova URL no sistema
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO cadastro (hits,nome,shortUrl,url)
    VALUES (?,?,?,?)
    """, (int(0), str(request.user),str(shortUrl),str(link_original)))
    conn.commit()
    conn.close()

def criar_funcao(shortUrl,url,host):
    final_url=shortUrl.replace(host,'')
    final_url=final_url.replace('/','')
    funcao='view_'+final_url
    html=f"""\"\"\"
<h1>
301 Redirect <br>
Location:{url}
<meta http-equiv="refresh" content="0; URL='{url}'"/>
</h1>
    \"\"\""""
    texto=f"""
def {funcao}(request):
    return HttpResponse({html})
    """
    with open('shorturl/views.py','a') as f:
        f.write(texto)
        f.close()
    criar_path(funcao,final_url)

def criar_path(funcao,final_url):
    texto=f"""path('{final_url}', short.{funcao}),"""
    with open('shorturl/path_functions.py','a') as f:
        f.write(texto)
        f.close()

def get_stats():
    # retorna estatisticas globais do sistema
    pass


def get_users_stats(user):
    """
    retorna as estatisticas das URLS de um usuário
    """
    # Conectando ao banco de dados
    conn = sqlite3.connect(pathdb)

    # Definindo cursor
    cursor = conn.cursor()

    # Achando o último valor
    cursor.execute(f"""
    SELECT *
    FROM cadastro 
    WHERE 
    nome='{str(user)}'
    Order BY hits asc;
    """)
    b=cursor.fetchall()[:]

    # Fechando banco de dados
    conn.close()
    return b

def stats_url(urlID):
    # retorna as estatisticas de uma URL específica
    pass


def delete_url(urlID):
    # deleta URL do sistema
    pass


def create_user(usuario):
    # cria um novo usuário
    pass
