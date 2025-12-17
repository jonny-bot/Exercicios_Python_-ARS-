# Importa a biblioteca CustomTkinter (uma versão moderna e estilizada do Tkinter)
import customtkinter

dx = 10
dy = 10

# Define o modo de aparência da interface (dark = modo escuro)
customtkinter.set_appearance_mode("dark")

# Define o tema de cores padrão (dark-blue = azul escuro)
customtkinter.set_default_color_theme("dark-blue")

# Cria a janela principal da aplicação
janela = customtkinter.CTk()

# Define o tamanho da janela (largura x altura)
janela.geometry("500x300")

# Função que será chamada quando o botão de login for clicado
def clique():
    print("Fazer Login")  # Apenas imprime no console

# Cria um rótulo (texto) na janela
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=dx, pady=dy)  # Adiciona o rótulo com espaçamento interno

# Cria um campo de entrada para o login
login = customtkinter.CTkEntry(janela, placeholder_text="Seu Login")
login.pack(padx=dx, pady=dy)

# Cria um campo de entrada para a senha (com caracteres ocultos)
senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=dx, pady=dy)

# Cria uma caixa de seleção (checkbox) para lembrar login
checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=dx, pady=dy)

# Cria um botão de login que chama a função 'clique' ao ser pressionado
botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=dx, pady=dy)

# Mantém a janela aberta e em execução (loop principal da interface gráfica)
janela.mainloop()
