import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(host='localhost', database='db_MeusLivros', user='root', password='Anninha16!')

Consulta_sql = "select * from tb_autores"
cursor = conexao.cursor
cursor.execute(Consulta_sql)
linhas = cursor.fetchall()
print("Número total de registros retornados:", rowcount)

print("\nMostrando os autores cadastrados")
for linha in linhas:
    print("Id:", linha[0])
     print("Nome:", linha[1])
      print("Sobrenome:", linha[2], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (conexao.is_connected()):
        conexao.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")

