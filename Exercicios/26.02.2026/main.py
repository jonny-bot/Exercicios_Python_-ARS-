import matplotlib.pyplot as plt

idade = [25,30,35,40,45,50]
salario = [3000,3500,40000,4500,5000,5500]

plt.scatter(idade, salario)

plt.title("Relação entre Idade-Salário")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.grid(True)