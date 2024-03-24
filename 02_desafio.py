# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# Instruções:
# 1 O programa deve começar solicitando ao usuário que insira seu nome.
print('Olá, tudo bem?')
nome = input("\nQual o seu nome? \n")

# 2 Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.

salario = float(input(f'\n{nome}, digite seu salário: \n'))

# 3 Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.

bonus = float(input("\nAgora, digite a % do seu bonus: \n"))

# 4 O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

fixo = 1000

calculo = ((fixo + salario)*bonus)

# 5 Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

print(f'\nOlá {nome}, o seu valor bônus foi de R$ {calculo:.2f}.')

# Exemplo de Saída:
# Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:


# Olá Luciano, o seu bônus foi de 8500


# 6 Salve esse script python como kpi.py
# 7 Faça uma documentação simples de como executar esse programa, utilize o README
# 8 Salve no Git e no Github
# 9 Isso ajudará a consolidar seu conhecimento sobre o Git e a familiarizar-se com o processo de versionamento de código.