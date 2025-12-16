xi = [23, 24, 25, 26]
fi = [7, 13, 8, 2]

xi_fi = [x * f for x, f in zip(xi, fi)]

soma_xi_fi = sum(xi_fi)

soma_fi = sum(fi)

media_ponderada = soma_xi_fi / soma_fi

print(f"Média aritmética ponderada: {media_ponderada:.2f}")
