import sqlite3

conexao = sqlite3.connect('banco-womakers')

cursor = conexao.cursor()


#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos (id int, nome VARCHAR (100), idade int, curso VARCHAR (50));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Helena", 21, "Farmácia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Felipe", 24, "Engenharia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Marcos Vinícios", 26, "Matemática");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Bruna", 19, "Enfermagem");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Maria Clara", 25, "Física");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Analice", 22, "Engenharia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (7, "Fernando", 26, "Engenharia");')


# Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
idades = cursor.execute('SELECT nome FROM alunos WHERE idade > 20')
for cada in idades:
    print(cada)


#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
engenheiros = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
for eng in engenheiros:
    print(eng)

#d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT (nome) FROM alunos')


#4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 19 WHERE id = 6')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 3')


#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes (id int, nome VARCHAR (100), idade int, saldo float);')

#ADIÇÃO DE REGISTROS
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "João", 24, 500);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Maria", 21, 1500);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Enrico", 43, 10000);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Bernardo", 65, 900);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Fábio", 56, 4000);')


#6. Consultas e Funções Agregadas
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
mais30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for mais in mais30:
    print(mais)

#b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT avg(saldo) FROM clientes')

#c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT nome WHERE saldo IN (SELECT max(saldo) FROM clientes) FROM clientes')

#d) Conte quantos clientes têm saldo acima de 1000
cursor.execute('SELECT nome, COUNT(*) FROM clientes WHERE saldo > 1000 GROUP BY nome')

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 1700 WHERE nome = "Maria" ')

#b) Remova um cliente pelo seu ID
cursor.execute('DELETE FROM clientes WHERE id = 1')



#8. Junção de Tabelas

#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras (id int, cliente_id int, produto VARCHAR (100), valor real);')

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 5, "Esteira", 2000);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, "Relógio", 1000);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "Celular", 3500);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 2, "Jóia", 500);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 4, "Camiseta", 50);')


juncao = cursor.execute('SELECT produto, valor, clientes.nome FROM compras LEFT JOIN clientes WHERE clientes.id = compras.cliente_id')
for client in juncao:
    print(client)


conexao.commit()
conexao.close()