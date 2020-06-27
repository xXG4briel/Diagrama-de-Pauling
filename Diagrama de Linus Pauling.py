from random import randint

s = ['', '', '', '', '', '', '']
p = ['', '', '', '', '', '']
d = ['', '', '', '']
f = ['', '']
texto = ['=-' * 35, 'Diagrama de Pauling']
print(f'\033[1:34m{texto[0]}\n{texto[1]: ^70}\n{texto[0]}')

Elemento = int(input('\nDigite um numero atômico: '))
if 0 < Elemento < 119:
    for i in range(1, Elemento + 1):
        if i <= 2:  # 1s2
            s[0] = f'1s{i}'
        elif i <= 4:  # 2s2
            s[1] = f'2s{i - 2}'
        elif i <= 10:  # 2p6
            p[0] = f'2p{i - 4}'
        elif i <= 12:  # 3s2
            s[2] = f'3s{i - 10}'
        elif i <= 18:  # 3p6
            p[1] = f'3p{i - 12}'
        elif i <= 20:  # 4s2
            s[3] = f'4s{i - 18}'
        elif i <= 30:  # 3d10
            d[0] = f'3d{i - 20}'
        elif i <= 36:  # 4p6
            p[2] = f'4p{i - 30}'
        elif i <= 38:  # 5s2
            s[4] = f'5s{i - 36}'
        elif i <= 48:  # 4d10
            d[1] = f'4d{i - 38}'
        elif i <= 54:  # 5p6
            p[3] = f'5p{i - 48}'
        elif i <= 56:  # 6s2
            s[5] = f'6s{i - 54}'
        elif i <= 70:  # 4f14
            f[0] = f'4f{i - 56}'
        elif i <= 80:  # 5d10
            d[2] = f'5d{i - 70}'
        elif i <= 86:  # 6p6
            p[4] = f'6p{i - 80}'
        elif i <= 88:  # 7s2
            s[6] = f'7s{i - 86}'
        elif i <= 102:  # 5f14
            f[1] = f'5f{i - 88}'
        elif i <= 112:  # 6d10
            d[3] = f'6d{i - 102}'
        elif i <= 118:  # 7p6
            p[5] = f'7p{i - 112}'
    x = randint(30, 37);
    cor = f'\033[1:{x}m'
    print(
        f'\n{cor}{s[0]}\n{s[1]} {p[0]}\n{s[2]} {p[1]} {d[0]}\n{s[3]} {p[2]} {d[1]} {f[0]}\n{s[4]} {p[3]} {d[2]} {f[1]}\n{s[5]} {p[4]} {d[3]}\n{s[6]} {p[5]}')
