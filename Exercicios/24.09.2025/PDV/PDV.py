from produtos import produtos
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk

# Tema escuro
BG_COLOR = "#2e2e2e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#4caf50"
ENTRY_BG = "#3c3c3c"

carrinho = []

def atualizar_lista_carrinho():
    carrinho_list.delete(0, tk.END)
    for i, item in enumerate(carrinho):
        produto = produtos[item["codigo"]]
        carrinho_list.insert(tk.END, f"{produto['nome']} x {item['quantidade']}")

def adicionar_ao_carrinho(codigo, quantidade_entry):
    try:
        quantidade = int(quantidade_entry.get())
        carrinho.append({"codigo": codigo, "quantidade": quantidade})
        atualizar_lista_carrinho()
        messagebox.showinfo("Sucesso", f"{produtos[codigo]['nome']} adicionado ao carrinho.")
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida.")

def remover_item():
    selecionado = carrinho_list.curselection()
    if selecionado:
        carrinho.pop(selecionado[0])
        atualizar_lista_carrinho()

def mostrar_resumo():
    total = 0
    resumo = ""
    for item in carrinho:
        produto = produtos[item["codigo"]]
        subtotal = produto["preco"] * item["quantidade"]
        total += subtotal
        resumo += f"{produto['nome']} x {item['quantidade']} = R$ {subtotal:.2f}\n"
    resumo += f"\nTotal: R$ {total:.2f}"
    messagebox.showinfo("Resumo da Compra", resumo)
    escolher_pagamento(total, resumo)

def escolher_pagamento(total, resumo):
    def aplicar_pagamento():
        opcao = pagamento_var.get()
        if opcao == "1":
            total_final = total * 0.95
            resultado = f"Total com desconto: R$ {total_final:.2f}"
        elif opcao == "2":
            try:
                parcelas = int(parcelas_entry.get())
                total_final = total * (1 + 0.02 * parcelas)
                valor_parcela = total_final / parcelas
                resultado = f"Total com juros: R$ {total_final:.2f}\n{parcelas}x de R$ {valor_parcela:.2f}"
            except ValueError:
                messagebox.showerror("Erro", "Número de parcelas inválido.")
                return
        else:
            messagebox.showerror("Erro", "Selecione uma opção válida.")
            return

        messagebox.showinfo("Pagamento", resultado)
        exportar_resumo(resumo + "\n\n" + resultado)

    pagamento_window = tk.Toplevel(root)
    pagamento_window.title("Forma de Pagamento")
    pagamento_window.configure(bg=BG_COLOR)

    pagamento_frame = ttk.Frame(pagamento_window, padding=10)
    pagamento_frame.pack()

    ttk.Label(pagamento_frame, text="Escolha a forma de pagamento:", foreground=FG_COLOR).grid(row=0, column=0, columnspan=2, pady=5)
    pagamento_var = tk.StringVar()
    ttk.Radiobutton(pagamento_frame, text="1 - À vista (5% de desconto)", variable=pagamento_var, value="1").grid(row=1, column=0, sticky="w")
    ttk.Radiobutton(pagamento_frame, text="2 - A prazo (2% de juros ao mês)", variable=pagamento_var, value="2").grid(row=2, column=0, sticky="w")

    parcelas_entry = ttk.Entry(pagamento_frame)
    parcelas_entry.grid(row=3, column=0, pady=5)
    parcelas_entry.insert(0, "Número de parcelas")

    ttk.Button(pagamento_frame, text="Confirmar", command=aplicar_pagamento).grid(row=4, column=0, pady=10)

def exportar_resumo(texto):
    caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de texto", "*.txt")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)
        messagebox.showinfo("Exportado", f"Resumo salvo em:\n{caminho}")

def iniciar_mercadinho():
    global root
    root = tk.Tk()
    root.title("🛒 Mercadinho do Bairro")
    root.configure(bg=BG_COLOR)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Arial", 10), foreground=FG_COLOR, background=BG_COLOR)
    style.configure("TButton", font=("Arial", 10), padding=5)
    style.configure("TEntry", font=("Arial", 10))
    style.configure("Produto.TFrame", background="#3a3a3a", relief="raised")

    # Área rolável
    canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    ttk.Label(scrollable_frame, text="🛍️ Produtos disponíveis:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    for i, (codigo, dados) in enumerate(produtos.items()):
        frame = ttk.Frame(scrollable_frame, padding=10, style="Produto.TFrame")
        frame.grid(row=(i//2)+1, column=i%2, padx=10, pady=10, sticky="nsew")

        try:
            imagem = Image.open(f"imagens/{codigo}.png")
            imagem = imagem.resize((80, 80))
            foto = ImageTk.PhotoImage(imagem)
            label_img = ttk.Label(frame, image=foto)
            label_img.image = foto
            label_img.grid(row=0, column=0, rowspan=3, padx=5)
        except:
            pass

        ttk.Label(frame, text=f"{codigo} - {dados['nome']}", foreground=FG_COLOR).grid(row=0, column=1, sticky="w")
        ttk.Label(frame, text=f"R$ {dados['preco']:.2f}", foreground=FG_COLOR).grid(row=1, column=1, sticky="w")

        quantidade_entry = ttk.Entry(frame, width=5)
        quantidade_entry.grid(row=2, column=1, sticky="w", pady=5)
        quantidade_entry.insert(0, "1")

        btn = tk.Button(frame, text="Adicionar", bg=BTN_COLOR, fg="white",
                        command=lambda c=codigo, q=quantidade_entry: adicionar_ao_carrinho(c, q))
        btn.grid(row=2, column=2, padx=5)

    ttk.Label(scrollable_frame, text="🛒 Carrinho de Compras", font=("Arial", 12, "bold")).grid(row=999, column=0, columnspan=2, pady=20)

    frame_carrinho = ttk.Frame(scrollable_frame)
    frame_carrinho.grid(row=1000, column=0, columnspan=2)

    scrollbar_carrinho = ttk.Scrollbar(frame_carrinho)
    scrollbar_carrinho.pack(side="right", fill="y")

    global carrinho_list
    carrinho_list = tk.Listbox(frame_carrinho, width=50, yscrollcommand=scrollbar_carrinho.set, bg=ENTRY_BG, fg=FG_COLOR)
    carrinho_list.pack(side="left")
    scrollbar_carrinho.config(command=carrinho_list.yview)

    ttk.Button(scrollable_frame, text="Remover Item Selecionado", command=remover_item).grid(row=1001, column=0, columnspan=2, pady=10)

    finalizar_btn = tk.Button(scrollable_frame, text="✅ Finalizar Compra", font=("Arial", 12, "bold"),
                              bg="#ff9800", fg="black", command=mostrar_resumo)
    finalizar_btn.grid(row=1002, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

    def piscar():
        cor = finalizar_btn.cget("bg")
        novo_cor = "#ffc107" if cor == "#ff9800" else "#ff9800"
        finalizar_btn.config(bg=novo_cor)
        root.after(500, piscar)

    piscar()
    root.mainloop()


# Tela de login
def autenticar():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if usuario == "joao" and senha == "ars@2025":
        login_window.destroy()
        iniciar_mercadinho()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

login_window = tk.Tk()
login_window.title("Login")
login_window.configure(bg=BG_COLOR)

ttk.Label(login_window, text="Usuário:").pack(pady=5)
usuario_entry = ttk.Entry(login_window)
usuario_entry.pack()

ttk.Label(login_window, text="Senha:").pack(pady=5)
senha_entry = ttk.Entry(login_window, show="*")
senha_entry.pack()

ttk.Button(login_window, text="Entrar", command=autenticar).pack(pady=10)

login_window.mainloop()
