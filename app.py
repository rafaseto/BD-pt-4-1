# link repositório github: <https://github.com/rafaseto/BD-pt-4-1.git>

import psycopg2

host = 'database-1.clidhukfcnn3.us-east-1.rds.amazonaws.com'

bd_nome = 'postgres'

usuario_01 = "rafaelseto"

senha_01 = 'professor'

# ====================
# Estabelecendo a conexão
conexao = psycopg2.connect(host=host, dbname=bd_nome, user=usuario_01, password=senha_01)
print('Criou a conexao')

# Objeto do tipo cursor, utilizado para executar comandos SQL
cursor = conexao.cursor()

# ====================
# MÉTODO PARA CONSULTAR TABELA 'departamento'
def consulta_departamento():
    # Instrução SELECT
    SQL_select = "SELECT * FROM mydb.departamento"
    
    # Executando a instrução SELECT
    cursor.execute(SQL_select)
    
    # Confirmando a transação
    conexao.commit()

    # Imprime registros retornados pela consulta SQL
    for linha in cursor:
        print(linha)

# ====================
# MÉTODO PARA INSERIR UMA LINHA NA TABELA 'departamento'
def insere_departamento(id, nome):
    # Instrução INSERT INTO
    SQL_insert = "INSERT INTO mydb.departamento VALUES (%s, %s)"

    # Executando a instrução INSERT INTO
    cursor.execute(SQL_insert, (id, nome))

    # Confirmando a transação
    conexao.commit()

# ====================
# TESTANDO OS MÉTODOS

# Inserindo o departamento "Cardiologia"
insere_departamento(9, "Cardiologia")

# Inserindo o departamento "Neurologia"
insere_departamento(10, "Neurologia")

# Consulta tabela "departamento"
consulta_departamento()