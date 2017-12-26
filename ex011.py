#Cálculo de gasto de tinta para uma parede (1L = 2m²)
l = float(input('Informe a largura da parede: '))
h = float(input('Informe a altura da parede: '))
a = l*h
print('A parede possui {:.2f}m² de área. Serão necessários {:.2f}L de tinta para esta parede.'.format(a, a/2))
