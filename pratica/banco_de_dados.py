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
  print('Nick', '|', linha[1], '|', 'Genero', '|', linha[3])