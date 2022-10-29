import webbrowser

site = str(input('Digite um site: '))
n = int(input('quantas vezes voce quer abrir o site: '))
for x in range(0, n):
 if site == site:
   n = webbrowser.open_new(site)
 else:
    print('não executado')