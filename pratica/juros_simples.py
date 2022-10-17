import colorama
from colorama import Fore
from colorama import Style

capital = int(input('Valor Inicial: '))
taxa = int(input('Taxa em Meses: '))
tempo = int(input('Tempo em Meses: '))

# Calculo juros simples
calc = capital * taxa / 100 * tempo

# Valor final com juros
final = calc + capital

print(Fore.BLUE + Style.BRIGHT + 'Valor Investido R${:.2f}'.format(capital) + Style.RESET_ALL)
print(Fore.GREEN + 'Valor Final R${:.2f}'.format(final) + Style.RESET_ALL)
print(Fore.RED + 'Valor com Juros R${:.2f}'.format(calc) + Style.RESET_ALL)