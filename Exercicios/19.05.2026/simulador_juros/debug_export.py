from exportacao import exportar_dados

print('exportacao module loaded successfully')

samples = ['R$ 1.234,56', 'R$ 12,50', '15%', '22,5%', '22,5', '1.234,56', '1,234.56', 'R$ 0,00', 'R$ 123456,78']
for s in samples:
    texto = str(s).strip()
    if texto.startswith('R$'):
        numero = texto.replace('R$', '').replace('.', '').replace(',', '.').strip()
        try:
            print(s, '->', numero, '->', float(numero))
        except Exception as e:
            print('ERROR', s, e)
    elif texto.endswith('%'):
        numero = texto.replace('%', '').replace('.', '').replace(',', '.').strip()
        try:
            print(s, '->', numero, '->', float(numero) / 100.0)
        except Exception as e:
            print('ERROR', s, e)
    else:
        numero = texto.replace('.', '').replace(',', '.')
        try:
            print(s, '->', numero, '->', float(numero))
        except Exception as e:
            print('ERROR', s, e)
