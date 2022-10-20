from calendar import isleap
from datetime import date
a = int(input('digite um ano: '))
if a == 0:
    a = date.today().year
if isleap(a):
    print('{} é bissexto'.format(a))
else:
    print('{} não é bissexto'.format(a))