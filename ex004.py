#Exibindo informações de uma string
var = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É um número? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É alfanumérico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizado? {}'.format(var.istitle()))
