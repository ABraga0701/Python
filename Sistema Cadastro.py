#Importar as bibliotecas

import tkinter as tk
from tkinter import ttk

import datetime as dt

lista_prod=["Boné", "Blusa", "Camiseta", "Perfume", "Chinelo"]
lista_cod=["BO001", "BL002", "CA003", "PE004", "CH005"]

#Criar interface grafica

janela = tk.Tk()

#Titulo janela 

janela.title('Sistema de cadastro de vendas')

label_codprod =tk.Label(text="Código produto")
label_codprod.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_selecionar_codprod = ttk.Combobox(values=lista_cod)
combobox_selecionar_codprod.grid(row=2, column=0,padx=10, pady=10, sticky='nswe', columnspan=1)

label_produto = tk.Label(text="Produto")
label_produto.grid(row=1,column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_selecionar_produto = ttk.Combobox(values=lista_prod)
combobox_selecionar_produto.grid(row=2, column=1,padx=10, pady=10, columnspan=2)

label_cliente =tk.Label(text="Cliente")
label_cliente.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_cliente =tk.Entry()
entry_cliente.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

label_unidade =tk.Label(text="Unidade de compra")
label_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_unidade =tk.Entry()
entry_unidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

label_preco =tk.Label(text="Preço")
label_preco.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_preco =tk.Entry()
entry_preco.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

#Criar botao para salvar

botao_salvar =tk.Button(text="Salvar")
botao_salvar.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
janela.mainloop()
