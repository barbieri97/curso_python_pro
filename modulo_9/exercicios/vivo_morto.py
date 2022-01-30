def vivo_morto(item):
    if item[1] == 'Dead':
        return f'{item[0]} está \033[1;31mmorto\033[0;0m '
    elif item[1] == 'Alive':
        return f'{item[0]} está \033[1;92mvivo\033[0;0m'
    else:
        return f'não sabemos se {item[0]} esta vivo ou morto'