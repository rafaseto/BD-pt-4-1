import psycopg2

host = 'database-1.clidhukfcnn3.us-east-1.rds.amazonaws.com'

bd_nome = 'postgres'

usuario_01 = "rafaelseto"

senha_01 = 'professor'

conexao = psycopg2.connect(host=host, dbname=bd_nome, user=usuario_01, password=senha_01)
print('Criou a conexao')

# Objeto do tipo cursor, utilizado para executar comandos SQL
cursor = conexao.cursor()

# Comando de teste SQL
SQL_insert_into = "INSERT INTO mydb.departamento (id_departamento, nome) VALUES (%s, %s)"

# Executando o comando de teste
cursor.execute(SQL_insert_into, (2, "DMA"))

# Confirma a transação
conexao.commit()

print("Dados inseridos com sucesso!")   

# Imprime registros retornados pela consulta SQL
# for record in cursor:
#    print(record)
