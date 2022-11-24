import os
import webbrowser

def main():
    while True:
        os.system("cls") #limpar a tela no terminal
        print("\nEscolha uma opção para executar : ")
        print("""
        1 : Abrir um site
        2 : Estudar Python
        3 : Enviar Curriculo
        4 : Planilha Videos
        5 : Editar Videos
        6 : Termius
        7 : Jogar COD Warzone
        8 : Pesquisa Twitter
        0 : Sair"""
              )
        choice = input("\nDigite sua escolha : ")

        if choice == '1':
            site = str(input('Digite um site para abrir: '))
            webbrowser.open(site, new=1)
        elif choice == '2' :
            curso = webbrowser.open('https://www.youtube.com/watch?v=N1hTsbW50eM&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=96', new=1)
            os.startfile('C:/Program Files/JetBrains/PyCharm Community Edition 2022.2.3/bin/pycharm64.exe')
        elif choice == '3' :
            vagas = webbrowser.open('https://empregos.maringa.com/?text=&estado=&cidade=&bairro=&tipo=&experiencia=N%C3%A3o&area=&faixa_salarial=')
        elif choice == '4' :
            planilha = webbrowser.open('https://docs.google.com/spreadsheets/d/1ZLQ1b0KdYFSjce4wm3o6-qbzHkHsG0g78bXNFULv76s/edit#gid=0')
        elif choice == '5' :
            os.startfile('E:/Adobe Premiere/Adobe Premiere Pro 2022/Adobe Premiere Pro.exe')
        elif choice == '6' :
            os.startfile('C:/Program Files/WindowsApps/Crystalnix.Termius_7.51.0.0_x64__0m0t0j9spf6x8/app/Termius.exe')
        elif choice == '7' :
            os.startfile('C:/Program Files (x86)/Battle.net/Battle.net Launcher.exe')
            os.startfile('D:\Call of Duty\Call of Duty Launcher.exe')
        elif choice == '8':
            twitch = str(input('Buscar: '))
            webbrowser.open(f'https://www.twitch.tv/search?term={twitch}')
        elif choice == '0':
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()
