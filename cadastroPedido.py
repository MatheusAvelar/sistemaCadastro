from tkinter import *
from tkinter import messagebox, ttk

#==== Janela ====#
janela = Tk()
janela.title("2G'S Burguer - Cadastro de Pedido")
janela.geometry("800x435")
janela.configure(background="white")
janela.resizable(width=False, height=False)

#==== Funções ====#
def Esconder(texto):
    texto.place(x=5000, y=5000)

#==== Imagens ====#
imgLogo = PhotoImage(file="icons/51x64.png")
imgIncluir = PhotoImage(file="icons/upload.png")
imgExcluir = PhotoImage(file="icons/lixeira.png")
janela.iconbitmap("icons/icon.ico")

#==== Frame ====#
Line = Label(janela,width=700, height=0)
Line.place(x=0, y=70)

#==== Cabeçalho ====#
TitleLabel = Label(text="Cadastro de Pedidos", font=("Century Gothic", 20), bg="White")
TitleLabel.place(x=70, y=10)
ImgLogo = Label(image=imgLogo, bg="White")
ImgLogo.place(x=10, y=0)


#==== Lista ====#
ListaProdutos = ["Combo Magrão + Refrigerante 500ml","Batata Frita"]

LbProdutos = Listbox(janela,height=15, width=45, xscrollcommand=True,yscrollcommand=True)

for produtos in ListaProdutos:
    LbProdutos.insert(END,produtos)

LbProdutos.place(x=500, y=100)

#==== Label ====#
LabelCodProduto = Label(text="Código do Catálogo:", font=("Century Gothic", 10), bg="White")
LabelCodProduto.place(x=11, y=100)
CodProduto = ttk.Entry(width=20)
CodProduto.place(x=15, y=125)

LabelProduto = Label(text="Produto:", font=("Century Gothic", 10), bg="White")
LabelProduto.place(x=11, y=150)
NomeProduto = Label(text="Combo Magrão + Refrigerante 500ml", font=("Century Gothic", 10), bg="White", justify=LEFT)
NomeProduto.place(x=11, y=170)

LabelDescricao = Label(text="Descrição:", font=("Century Gothic", 10), bg="White")
LabelDescricao.place(x=11, y=190)
NomeDescricao = Label(text="- 300g de Bacon moído\n" +
                            "- Alface\n" +
                            "- Frango Desfiado\n" + 
                            "- Ovo\n" +
                            "- Refrigerante Lata 500ml\n", font=("Century Gothic", 8), bg="White", justify=LEFT)
NomeDescricao.place(x=11, y=210)

LabelValUnitario = Label(text="Valor Unitário:", font=("Century Gothic", 10), bg="White")
LabelValUnitario.place(x=11, y=350)
ValUnitario = Label(text="R$30,00", font=("Century Gothic", 10), bg="White")
ValUnitario.place(x=110, y=350)

LabeQuantidade = Label(text="Quantidade:", font=("Century Gothic", 10), bg="White")
LabeQuantidade.place(x=200, y=350)
Quantidade = ttk.Entry(width=10)
Quantidade.place(x=290, y=350)

LabelValTotal = Label(text="Valor Total:", font=("Century Gothic", 10), bg="White")
LabelValTotal.place(x=550, y=400)
ValTotal = Label(text="R$40,00", font=("Century Gothic", 20), bg="White")
ValTotal.place(x=650, y=390)

ImgInserir = Label(image=imgIncluir, bg="White")
ImgInserir.place(x=720, y=350)
ImgRetirar = Label(image=imgExcluir, bg="White")
ImgRetirar.place(x=750, y=350)

QuitButton = ttk.Button(text="Sair",width=10, command=quit)
QuitButton.place(x=260,y=400)
ConfirmButton = ttk.Button(text="Confirmar",width=10, command=quit)
ConfirmButton.place(x=340,y=400)

#==== Execução ====#
janela.mainloop()