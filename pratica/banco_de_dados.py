import pymysql.cursors

#conexao
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='eleicoes'
)

cursor = conexao.cursor()
sql = "SELECT * FROM presidentes"
cursor.execute(sql)
resultado = cursor.fetchall()

for linha in resultado:
  print('='*20)
  print('Nick', '|','Genero', '|')
  print(linha[1], '|', linha[3])

# melhor script
# criar um menu de cadastro e de leitura dentro desse script / com while, if else