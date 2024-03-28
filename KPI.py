# Solicitar o nome do usuário
print('Olá, tudo bem?')
nome = input("\nQual o seu nome? \n")

# Solicitar o salário do usuário
salario = float(input(f'\n{nome}, digite seu salário: \n'))

# Solicitar a % do bônus do usuário
bonus = float(input("\nAgora, digite a % do seu bonus: \n"))

# Comissão fixa
fixo = 1000

# Cálculo do KPI
calculo = fixo + (salario*bonus)

# Devolução do valor calculado para o usuário
print(f'\nOlá {nome}, o seu valor bônus foi de R$ {calculo:.2f}.')
