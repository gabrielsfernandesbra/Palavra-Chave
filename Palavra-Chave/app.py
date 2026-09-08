import customtkinter as ctk
from tkinter import messagebox
import string
import secrets

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

cor_fundo = "#0B0D10"
cor_cinza = "#555D68"
cor_azul = "#00A8FF"
cor_texto = "#F2F4F7"

app = ctk.CTk()
app.title("PALAVRA CHAVE")
app.geometry("430x570")
app.resizable(False, False)
app.configure(fg_color=cor_fundo)

# =================================================================

senha = ""

def gerar():
    global senha
    maior = string.ascii_uppercase
    menor = string.ascii_lowercase
    numero = "1234567890"
    simbolo = "@!#*_-.$%&?/"
    combinar = ""
    obrigatorios = []

    if status_1.get():
        combinar += maior
        obrigatorios.append(maior)
    if status_2.get():
        combinar += menor
        obrigatorios.append(menor)
    if status_3.get():
        combinar += numero
        obrigatorios.append(numero)
    if status_4.get():
        combinar += simbolo
        obrigatorios.append(simbolo)

    if not combinar:
        messagebox.showwarning("Atenção", "Selecione pelo menos uma opção!")
        return

    comprimento = int(spin.get())

    if comprimento < len(obrigatorios):
        messagebox.showwarning("Atenção", f"Escolha um tamanho de pelo menos {len(obrigatorios)} caracteres!")
        return

    senha_lista = [secrets.choice(tipo) for tipo in obrigatorios]
    senha_lista += [secrets.choice(combinar) for _ in range(comprimento - len(senha_lista))]
    secrets.SystemRandom().shuffle(senha_lista)

    senha = "".join(senha_lista)
    senha_label.configure(text=senha)

def copiar():
    if not senha:
        messagebox.showwarning("Atenção", "Gere uma senha primeiro!")
        return

    app.clipboard_clear()
    app.clipboard_append(senha)
    app.update()
    copiar_button.configure(text="✓ Copiado")
    app.after(1500, lambda: copiar_button.configure(text="Copiar"))

# =================================================================

header = ctk.CTkFrame(app, fg_color="transparent")
header.pack(fill="x", padx=30, pady=(28, 15))

logo = ctk.CTkLabel(header, text="🔐", font=ctk.CTkFont(size=30))
logo.pack(side="left")

titulo_frame = ctk.CTkFrame(header, fg_color="transparent")
titulo_frame.pack(side="left", padx=12)

titulo = ctk.CTkLabel(titulo_frame, text="GERADOR DE SENHAS", font=ctk.CTkFont(size=24, weight="bold"), text_color=cor_texto)
titulo.pack(anchor="w")

subtitulo = ctk.CTkLabel(titulo_frame, text="Gerador de senhas seguras", font=ctk.CTkFont(size=12), text_color=cor_cinza)
subtitulo.pack(anchor="w")

card = ctk.CTkFrame(app, fg_color=cor_fundo, corner_radius=18, border_width=1, border_color=cor_cinza)
card.pack(fill="both", expand=True, padx=25, pady=(5, 25))

senha_titulo = ctk.CTkLabel(card, text="SUA SENHA", font=ctk.CTkFont(size=11, weight="bold"), text_color=cor_cinza)
senha_titulo.pack(anchor="w", padx=25, pady=(25, 8))

senha_frame = ctk.CTkFrame(card, fg_color=cor_cinza, corner_radius=12, height=58)
senha_frame.pack(fill="x", padx=25)
senha_frame.pack_propagate(False)

senha_label = ctk.CTkLabel(senha_frame, text="Gere sua senha...", font=ctk.CTkFont(size=16, weight="bold"), text_color=cor_texto)
senha_label.pack(side="left", padx=18)

copiar_button = ctk.CTkButton(senha_frame, text="Copiar", width=75, height=34, corner_radius=8, fg_color=cor_azul, hover_color=cor_azul, font=ctk.CTkFont(size=12, weight="bold"), command=copiar)
copiar_button.pack(side="right", padx=10)

tamanho_frame = ctk.CTkFrame(card, fg_color="transparent")
tamanho_frame.pack(fill="x", padx=25, pady=(22, 10))

tamanho_label = ctk.CTkLabel(tamanho_frame, text="Tamanho da senha", font=ctk.CTkFont(size=13, weight="bold"), text_color=cor_texto)
tamanho_label.pack(side="left")

# =================================================================

spin = ctk.CTkComboBox(tamanho_frame, values=[str(i) for i in range(4, 21)], width=75, height=35, corner_radius=8, fg_color=cor_cinza, border_color=cor_cinza, button_color=cor_azul, button_hover_color=cor_azul, text_color=cor_texto, justify="center")
spin.set("12")
spin.pack(side="right")

opcoes_label = ctk.CTkLabel(card, text="TIPOS DE CARACTERES", font=ctk.CTkFont(size=11, weight="bold"), text_color=cor_cinza)
opcoes_label.pack(anchor="w", padx=25, pady=(15, 8))

opcoes_frame = ctk.CTkFrame(card, fg_color="transparent")
opcoes_frame.pack(fill="x", padx=20)

# =================================================================

status_1 = ctk.BooleanVar(value=True)
status_2 = ctk.BooleanVar(value=True)
status_3 = ctk.BooleanVar(value=True)
status_4 = ctk.BooleanVar(value=True)

check_1 = ctk.CTkCheckBox(opcoes_frame, text="Maiúsculas", variable=status_1, checkbox_width=20, checkbox_height=20, corner_radius=5, fg_color=cor_azul, hover_color=cor_azul, border_color=cor_cinza, text_color=cor_texto, font=ctk.CTkFont(size=12))
check_1.grid(row=0, column=0, sticky="w", padx=5, pady=7)

check_2 = ctk.CTkCheckBox(opcoes_frame, text="Minúsculas", variable=status_2, checkbox_width=20, checkbox_height=20, corner_radius=5, fg_color=cor_azul, hover_color=cor_azul, border_color=cor_cinza, text_color=cor_texto, font=ctk.CTkFont(size=12))
check_2.grid(row=0, column=1, sticky="w", padx=15, pady=7)

check_3 = ctk.CTkCheckBox(opcoes_frame, text="Números", variable=status_3, checkbox_width=20, checkbox_height=20, corner_radius=5, fg_color=cor_azul, hover_color=cor_azul, border_color=cor_cinza, text_color=cor_texto, font=ctk.CTkFont(size=12))
check_3.grid(row=1, column=0, sticky="w", padx=5, pady=7)

check_4 = ctk.CTkCheckBox(opcoes_frame, text="Símbolos", variable=status_4, checkbox_width=20, checkbox_height=20, corner_radius=5, fg_color=cor_azul, hover_color=cor_azul, border_color=cor_cinza, text_color=cor_texto, font=ctk.CTkFont(size=12))
check_4.grid(row=1, column=1, sticky="w", padx=15, pady=7)

botao1 = ctk.CTkButton(card, command=gerar, text="Gerar senha", height=48, corner_radius=12, fg_color=cor_azul, hover_color=cor_azul, font=ctk.CTkFont(size=14, weight="bold"))
botao1.pack(fill="x", padx=25, pady=(25, 25))

rodape = ctk.CTkLabel(app, text="BY GABRIEL S FERNANDES", font=ctk.CTkFont(size=14), text_color=cor_cinza)
rodape.place(relx=0.5, rely=0.97, anchor="center")

# =================================================================

app.mainloop()
