def recall_password(cipher_grille, ciphered_password):
    plain = ''

    target = [[True if x == 'X' else False for x in row] for row in cipher_grille]

    for n in range(4):
        for i in range(len(target)):
            for j in range(len(target[i])):
                if target[i][j]:
                    plain += ciphered_password[i][j]
        target = list(zip(*reversed(target)))

    return plain

if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
