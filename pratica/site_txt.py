import webbrowser

with open("links.txt") as x:
    for url in x:
        webbrowser.open_new_tab(url.strip())