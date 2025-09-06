from math import radians, sin, cos, tan

angulo = int(input('Informe o angulo: '))

ang_radiano = radians(angulo)

seno = sin(ang_radiano)

cosseno = cos(ang_radiano)

tangente = tan(ang_radiano)

print(f'Seno: {seno:.4f}')

print(f'Cosseno: {cosseno:.4f}')

print(f'Tangente: {tangente:.4f}')