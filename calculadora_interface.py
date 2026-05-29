from tkinter import *
import math

historico = []

def clique(valor):
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, atual + valor)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        historico.append(f"{expressao} = {resultado}")
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
        atualizar_historico()
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, END)

def apagar():
    atual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, atual[:-1])

def porcentagem():
    try:
        resultado = float(entrada.get()) / 100
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Erro")

def raiz():
    try:
        resultado = math.sqrt(float(entrada.get()))
        entrada.delete(0, END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, END)
        entrada.insert(0, "Erro")

def atualizar_historico():
    lista_historico.delete(0, END)
    for item in historico[-5:]:
        lista_historico.insert(0, item)

def teclado(event):
    if event.char in "0123456789.+-*/":
        clique(event.char)
    elif event.keysym == "Return":
        calcular()
    elif event.keysym == "BackSpace":
        apagar()
    elif event.keysym == "Escape":
        limpar()


janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")
janela.bind("<Key>", teclado)

entrada = Entry(janela, font=("Arial", 28), width=16, justify="right",
                bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    ("C", "#e74c3c", limpar),
    ("⌫", "#e67e22", apagar),
    ("%", "#3498db", porcentagem),
    ("√", "#3498db", raiz),
    ("7", "#3d3d3d", lambda: clique("7")),
    ("8", "#3d3d3d", lambda: clique("8")),
    ("9", "#3d3d3d", lambda: clique("9")),
    ("/", "#e67e22", lambda: clique("/")),
    ("4", "#3d3d3d", lambda: clique("4")),
    ("5", "#3d3d3d", lambda: clique("5")),
    ("6", "#3d3d3d", lambda: clique("6")),
    ("*", "#e67e22", lambda: clique("*")),
    ("1", "#3d3d3d", lambda: clique("1")),
    ("2", "#3d3d3d", lambda: clique("2")),
    ("3", "#3d3d3d", lambda: clique("3")),
    ("-", "#e67e22", lambda: clique("-")),
    ("0", "#3d3d3d", lambda: clique("0")),
    (".", "#3d3d3d", lambda: clique(".")),
    ("=", "#2ecc71", calcular),
    ("+", "#e67e22", lambda: clique("+")),
]

row, col = 1, 0
for texto, cor, cmd in botoes:
    btn = Button(janela, text=texto, font=("Arial", 18), width=4, height=2,
                 bg=cor, fg="white", relief=FLAT, command=cmd,
                 activebackground=cor, activeforeground="white")
    btn.grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col == 4:
        col = 0
        row += 1

Label(janela, text="Histórico", font=("Arial", 10),
      bg="#1e1e1e", fg="#aaaaaa").grid(row=row, column=0, columnspan=4)

lista_historico = Listbox(janela, font=("Arial", 11), width=30, height=5,
                          bg="#2d2d2d", fg="#ffffff", bd=0)
lista_historico.grid(row=row+1, column=0, columnspan=4, padx=10, pady=5)

janela.mainloop()