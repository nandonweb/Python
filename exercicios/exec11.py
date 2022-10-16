l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

paredeM2 = l * a
tinta = paredeM2 / 2

print('Para pintar {}m² você precisa de {}L de tinta'.format(paredeM2, tinta))