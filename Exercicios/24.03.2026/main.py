import tkinter as tk
from tkinter import messagebox

def escolher_modelo():
    tipo = tipo_var.get()
    lineares = lineares_var.get()
    muitos_dados = muitos_var.get()
    prever = prever_var.get()

    if tipo == "Classificação":
        if lineares == "Sim":
            modelo = "LogisticRegression"
        else:
            if muitos_dados == "Sim":
                modelo = "RandomForestClassifier"
            else:
                modelo = "SVC, DecisionTreeClassifier, GradientBoostingClassifier"
    elif tipo == "Regressão":
        if lineares == "Sim":
            modelo = "LinearRegression, Ridge, Lasso"
        else:
            modelo = "SVR, RandomForestRegressor, GradientBoostingRegressor"
    elif tipo == "Clusterização":
        if prever == "Sim":
            modelo = "LinearRegression, SVR"
        else:
            modelo = "KMeans, DBSCAN, AgglomerativeClustering"
    else:
        modelo = "Tipo de problema não reconhecido"

    messagebox.showinfo("Sugestão de Modelo", f"Modelos sugeridos: {modelo}")

# Janela principal
root = tk.Tk()
root.title("Escolha de Modelo - Scikit-Learn")

# Variáveis
tipo_var = tk.StringVar(value="Classificação")
lineares_var = tk.StringVar(value="Não")
muitos_var = tk.StringVar(value="Não")
prever_var = tk.StringVar(value="Não")

# Widgets
tk.Label(root, text="Tipo de Problema:").pack()
tk.OptionMenu(root, tipo_var, "Classificação", "Regressão", "Clusterização").pack()

tk.Label(root, text="Dados Lineares?").pack()
tk.OptionMenu(root, lineares_var, "Sim", "Não").pack()

tk.Label(root, text="Muitos Dados?").pack()
tk.OptionMenu(root, muitos_var, "Sim", "Não").pack()

tk.Label(root, text="Prever Valores? (para clusterização)").pack()
tk.OptionMenu(root, prever_var, "Sim", "Não").pack()

tk.Button(root, text="Escolher Modelo", command=escolher_modelo).pack()

root.mainloop()
