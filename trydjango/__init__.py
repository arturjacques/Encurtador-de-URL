import sqlite3

pathdb='db/users'
nome_tabela='cadastro'

#Conectando ao banco de dados ou criando e conectando
conn = sqlite3.connect(pathdb)

#Definindo cursor
cursor = conn.cursor()

try:

    cursor.execute(f"""
SELECT * FROM {nome_tabela};
""")

except:
    cursor.execute(f"""
    CREATE TABLE {nome_tabela}(
    id INTEGER TEXT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    hits Integer,
    url TEXT NOT NULL,
    shortUrl TEXT NOT NULL
    );
    """)

#Fechando banco de dados
conn.close()
