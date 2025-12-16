serie = [3, 4, 7, 9]

media = sum(serie) / len(serie)

print(f'Média = {media}')

print(f'|x1 - x| = |3 - {media}| = {abs(serie[0] - media)}')
print(f'|x2 - x| = |4 - {media}| = {abs(serie[1] - media)}')
print(f'|x3 - x| = |7 - {media}| = {abs(serie[2] - media)}')
print(f'|x4 - x| = |9 - {media}| = {abs(serie[3] - media)}')
