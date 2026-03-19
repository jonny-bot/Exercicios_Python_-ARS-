# Criar interface gráfica para o programa de cadastro de clientes
import tkinter as tk
from tkinter import messagebox

class CadastroClientes:

    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Clientes")

        self.clientes = []  # Lista para armazenar os clientes cadastrados

        # Nome
        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        # E-Mail
        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=1, column=0)

        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=1, column=1)

        # Telefone
        self.label_telefone = tk.Label(master, text="Telefone:")
        self.label_telefone.grid(row=2, column=0)

        self.entry_telefone = tk.Entry(master)
        self.entry_telefone.grid(row=2, column=1)

        # Idade
        self.label_idade = tk.Label(master, text="Idade:")
        self.label_idade.grid(row=3, column=0)

        self.entry_idade = tk.Entry(master)
        self.entry_idade.grid(row=3, column=1)

        self.button_cadastrar = tk.Button(master, text="Cadastrar", command=self.cadastrar_cliente)
        self.button_cadastrar.grid(row=4, column=0, columnspan=2)

        self.button_consultar = tk.Button(master, text="Consultar Clientes", command=self.consultar_clientes)
        self.button_consultar.grid(row=5, column=0, columnspan=2)

    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()
        idade_str = self.entry_idade.get()

        if not nome or not email or not telefone or not idade_str:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            idade = int(idade_str)
            if idade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro positivo.")
            return

        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        self.clientes.append({'nome': nome, 'email': email, 'telefone': telefone, 'idade': idade})
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)

    def consultar_clientes(self):
        if not self.clientes:
            messagebox.showinfo("Consulta", "Nenhum cliente cadastrado ainda.")
            return

        # Criar nova janela para mostrar os clientes
        consulta_window = tk.Toplevel(self.master)
        consulta_window.title("Clientes Cadastrados")

        text_area = tk.Text(consulta_window, height=15, width=50)
        text_area.pack(pady=10, padx=10)

        for i, cliente in enumerate(self.clientes, start=1):
            text_area.insert(tk.END, f"Cliente {i}:\n")
            text_area.insert(tk.END, f"  Nome: {cliente['nome']}\n")
            text_area.insert(tk.END, f"  Email: {cliente['email']}\n")
            text_area.insert(tk.END, f"  Telefone: {cliente['telefone']}\n")
            text_area.insert(tk.END, f"  Idade: {cliente['idade']}\n\n")

        text_area.config(state=tk.DISABLED)  # Tornar somente leitura

if __name__ == "__main__":
    root = tk.Tk()
    cadastro_clientes = CadastroClientes(root)
    root.mainloop()
