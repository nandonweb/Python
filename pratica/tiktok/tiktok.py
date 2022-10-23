import webbrowser
import time
import sys

opcao = int(input('Escolha uma opcao \n1 - Hacker \n2 - Arregar = '))

if opcao == 1:
    print("Hackeando:")
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
    webbrowser.open("https://google.com")
else:
 print('FBI Open Up')
