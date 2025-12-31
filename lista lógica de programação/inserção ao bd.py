import mysql.connector
from mysql.connector import Error

try:
    cnx = mysql.connector.connect(host='localhost', database='db_meusprodutos', user='root', password='Anninha16!')
    consulta_sql = "select * from produtos"
    cursor = cnx.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount())

    print("\nMostrar os produtos cadastrados\n")
    for linha in linhas:
        print("id_produto:", linha[0])
        print("nome_produto:", linha[1])
        print("valor", linha[2])
        print("quantidade", linha[3], "\n")

except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (cnx.is_connected()):
        cursor.close()
        cnx.close()
        print("Conexão MySQL finalizada")
                            
