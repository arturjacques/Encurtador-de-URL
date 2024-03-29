import requests
import sqlite3
import json
import time

pathdb = 'db/users'


def verificacao_site(link):
    """
    Essa função pode ser a etapa mais lenta de toda a criação de URL.
    :return: Retorna True se o site está no ar e False se está fora do ar ou não existe
    """
    try:
        a = requests.get(link)
    except Exception:
        return False
    else:
        return True



def criar_shorturl():
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
    SELECT COUNT(id)
    FROM cadastro 
    """)
    a = int(cursor.fetchall()[0][0]) + 1

    # Criando a url com o último valor da sequência +1
    a = conversor(a)

    # Fechando banco de dados
    conn.close()

    return a


def conversor(a):
    numeros = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(numeros)

    convertido = ''

    while a >= base:
        resto = a % base
        convertido = numeros[resto] + convertido
        a = int(a / base)

    convertido = numeros[a] + convertido

    return convertido


def post(request, link_original):
    # criar função para redirecionar
    # Criar nova URL
    shortUrl = criar_shorturl()
    criar_funcao(shortUrl, link_original, request.get_host())
    # cadastra uma nova URL no sistema
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO cadastro (id,hits,nome,shortUrl,url)
    VALUES (?,?,?,?,?)
    """, (str(shortUrl), int(0), str(request.user), str(request.get_host() + '/' + shortUrl), str(link_original)))
    conn.commit()
    conn.close()
    x = {
        'id': str(shortUrl),
        'hits': 0,
        'url': str(link_original),
        'shortUrl': str(request.get_host() + '/' + shortUrl)
    }
    y = json.dumps(x)
    return json.dumps(x)


def criar_funcao(shortUrl, url, host):
    funcao = 'view_' + shortUrl
    html = f"""\"\"\"
<h1>
301 Redirect <br>
Location:{url}
<meta http-equiv="refresh" content="0; URL='{url}'"/>
</h1>
    \"\"\""""
    texto = f"""
def {funcao}(request):
    funcoes.add_visita(\'{shortUrl}\')
    return HttpResponse({html})

    """
    with open('shorturl/views.py', 'a') as f:
        f.write(texto)
        f.close()
    criar_path(funcao, shortUrl)


def criar_path(funcao, final_url):
    texto = f"""path('{final_url}', short.{funcao}),"""
    with open('shorturl/path_functions.py', 'a') as f:
        f.write(texto)
        f.close()


def add_visita(identificador):
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute(f"""
    update cadastro
    set hits=hits+1
    where id='{identificador}'
    """)
    conn.commit()
    conn.close()


def get_stats():
    # retorna estatisticas globais do sistema
    dados_globais = dict()
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT hits
    FROM cadastro
    """)
    hits = cursor.fetchall()

    soma = 0
    for i in hits:
        soma += i[0]
    dados_globais['hits'] = soma
    dados_globais['urlCount'] = len(hits)

    cursor.execute("""
    SELECT id
    FROM cadastro
    ORDER BY
    HITS DESC
    LIMIT 10
    """)
    top_ids = cursor.fetchall()
    dados_globais['topUrls'] = list()
    conn.close()
    for i in top_ids:
        dados_globais['topUrls'].append(json.loads(get_stats_id(i[0])))
    dados_globais=json.dumps(dados_globais)
    return dados_globais


def get_users_stats(user):
    """
    retorna as estatisticas das URLS de um usuário
    """
    listaUrl=list()
    # Conectando ao banco de dados
    conn = sqlite3.connect(pathdb)

    # Definindo cursor
    cursor = conn.cursor()

    # Achando o último valor
    cursor.execute(f"""
    SELECT id
    FROM cadastro 
    WHERE 
    nome='{str(user)}'
    Order BY hits desc;
    """)
    for i in cursor.fetchall():
        listaUrl.append(get_stats_id(i[0]))
    # Fechando banco de dados
    conn.close()
    return listaUrl


def get_stats_id(ID):
    dados = {}
    # retorna as estatisticas de uma URL específica
    conn = sqlite3.connect(pathdb)
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT *
    FROM cadastro
    where id='{str(ID)}'
    """)
    a = cursor.fetchone()
    dados['id'] = a[0]
    dados['hits'] = a[2]
    dados['url'] = a[3]
    dados['shortUrl'] = a[4]
    conn.close()
    dados = json.dumps(dados)
    return dados


def delete_url(ID):
    # deleta URL do sistema
    # deletar no path
    with open('shorturl/path_functions.py', 'r') as f:
        a = f.read().replace(f",path('{ID}', short.view_{ID})","")
        print(a)
        with open('shorturl/path_functions.py', 'w') as f:
            f.write(a)
    # deletar no bd
    return []


def create_user(usuario):
    # cria um novo usuário
    pass


def printar(x):
    print(60 * '-')
    print(x)
    print(60 * '-')
