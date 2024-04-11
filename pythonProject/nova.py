import tkinter as tk
from tkinter import messagebox

def exibir_mensagem_tkinter():
    messagebox.showinfo("mensagem", "mensagem usando tkinter!")

def exibir_conteudo():
    nome = campo_nome.get(
    sobrenome = campo_sobrenome.get()
    print('nome:', nome)
    print('sobrenome', sbrenome)
    )

#criando janela  com tk
janela_tkinter = tk.Tk()
janela_tkinter.title("Form")

janela_tkinter.geometry("800x300")

botao_tkinter = tk.Button(janela_tkinter, text="clica aqui (tkinter)", command=exibir_mensagem_tkinter)
botao_tkinter.pack()

#label
label_nome = tk.label(janela_tkinter, text="nome:")
label_nome.pack()

#imput
campo_nome = tk.Entry(janela_tkinter)
campo_nome.pack()

#sobrenome label
label_sobrenome = tk.label(janela_tkinter, text="sobrenome:")
label_sobrenome.pack()

#sobrenome campo
campo_sobrenome = tk.Entry(janela_tkinter)
campo_sobrenome.pack()

botao_exibir = tk.Button(janela_tkinter)


janela_tkinter.mainloop()
