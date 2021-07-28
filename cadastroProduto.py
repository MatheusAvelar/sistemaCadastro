from tkinter import *
from tkinter import messagebox, ttk

#==== Janela ====#
janela = Tk()
janela.title("2G'S Burguer - Cadastro de Produtos")
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
TitleLabel = Label(text="Cadastro de Produtos", font=("Century Gothic", 20), bg="White")
TitleLabel.place(x=70, y=10)
ImgLogo = Label(image=imgLogo, bg="White")
ImgLogo.place(x=10, y=0)

#==== Label Codigo ====#
LabelCodProduto = Label(text="Código do Catálogo:", font=("Century Gothic", 10), bg="White")
LabelCodProduto.place(x=11, y=100)
CodProduto = ttk.Entry(width=10)
CodProduto.place(x=160, y=100)
CodProduto.insert(0,1)
CodProduto.configure(state='disabled')
#==== Label Nome Produto ====#
LabelNomeProduto = Label(text="Nome do Produto:", font=("Century Gothic", 10), bg="White")
LabelNomeProduto.place(x=11, y=150)
nomeProduto = ttk.Entry(width=100)
nomeProduto.place(x=150, y=150)
#==== Label Descrição ====#
LabelDescricao = Label(text="Descrição:", font=("Century Gothic", 10), bg="White")
LabelDescricao.place(x=11, y=190)
Descricao = Text(janela,height=4, width=75)
Descricao.place(x=150, y=190)
#==== Label Valor Unitário ====#
LabelValUnitario = Label(text="Valor Unitário:", font=("Century Gothic", 10), bg="White")
LabelValUnitario.place(x=11, y=300)
ValUnitario = ttk.Entry(width=100)
ValUnitario.place(x=150, y=300)

#==== Funçoes ====#
codigo = int(CodProduto.get())
DicionarioProd = {}
DicionarioDesc = {}
DicionarioVal = {}
def Cadastrar():
    codigo = int(CodProduto.get())
    nomeProd = nomeProduto.get()
    descProd = Descricao.get("1.0",END)
    valProd = ValUnitario.get()
    DicionarioProd.update({codigo : nomeProd})
    DicionarioDesc.update({codigo : descProd})
    DicionarioVal.update({codigo : valProd})
    #==== Impressão para Testes ====#
    #indiceProd = len(DicionarioProd) - 1
    ultimoProd = DicionarioProd[codigo]
    ultimoDesc = DicionarioDesc[codigo]
    ultimoVal = DicionarioVal[codigo]
    print("Codigo:",codigo,"\nProduto:",ultimoProd,"\nDescrição:",ultimoDesc,"\nValor:",ultimoVal)
    #==== Contador Codigo ====#
    CodProduto.configure(state='enabled')
    codigo += 1
    CodProduto.delete(0,END)
    CodProduto.insert(END,codigo)
    #==== Mensagem ====#
    Mensagem["text"] = "Item Cadastrado!"
    Mensagem["foreground"] = "Green"
    #==== Limpa Campos ====#
    nomeProduto.delete(END)
    Descricao.delete(END)
    ValUnitario.delete(END)
    #==== Habilita Readonly ====#
    CodProduto.configure(state='disabled')
    

def RemoveProd(key):
    if int(key) >= 0 :
        print("Chave para deleção:",key)
        del DicionarioProd[key]
        Mensagem["foreground"] = "Red"
        Mensagem["text"] = "Item Removido!"

#==== Botões ====#
QuitButton = ttk.Button(text="Sair", width=10, command=quit)
QuitButton.place(x=260,y=400)
ConfirmButton = ttk.Button(text="Cadastrar", width=10, command=Cadastrar)
ConfirmButton.place(x=340,y=400)
#RemoveButton = ttk.Button(text="Remover", width=10, command=lambda: RemoveProd(codigo))
#RemoveButton.place(x=420,y=400)
Mensagem = Label(text="", font=("Century Gothic", 10), bg="White")
Mensagem.place(x=500,y=405)

#==== Execução ====#
janela.mainloop()