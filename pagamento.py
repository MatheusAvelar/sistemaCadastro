from tkinter import *
from tkinter import messagebox, ttk

#==== Janela ====#
janela = Tk()
janela.title("2G'S Burguer - Pagamento")
janela.geometry("500x435")
janela.configure(background="white")
janela.resizable(width=False, height=False)

#==== Funções ====#
def Esconder(texto):
    texto.place(x=5000, y=5000)

#==== Imagens ====#
imgDinheiro = PhotoImage(file="icons/dinheiro.png")
imgCredito = PhotoImage(file="icons/cartaoCredito.png")
imgDebito = PhotoImage(file="icons/cartaoDebito.png")
imgLogo = PhotoImage(file="icons/51x64.png")
janela.iconbitmap("icons/icon.ico")

#==== Frame ====#
Line = Label(janela,width=700, height=0)
Line.place(x=0, y=70)
Line = Label(janela,width=700, height=0)
Line.place(x=0, y=185)
Line = Label(janela,width=700, height=0)
Line.place(x=0, y=300)
Line = Label(janela,width=700, height=0)
Line.place(x=0, y=415)

#==== Cabeçalho ====#
TitleLabel = Label(text="Pagamento", font=("Century Gothic", 20), bg="White")
TitleLabel.place(x=70, y=10)
ImgLogo = Label(image=imgLogo, bg="White")
ImgLogo.place(x=10, y=0)

#==== Label Dinheiro ====#
ImgDinheiro = Label(image=imgDinheiro, bg="White")
ImgDinheiro.place(x=50, y=100)
LabelDinheiro = Label(text="Dinheiro", font=("Century Gothic", 10), bg="White")
LabelDinheiro.place(x=120, y=135)
ValDinheiro = Label(text="R$ 200,00", font=("Century Gothic", 20), bg="White")
ValDinheiro.place(x=350, y=100)

#==== Label Credito ====#
ImgLabel = Label(image=imgCredito, bg="White")
ImgLabel.place(x=50, y=215)
LabelCredito = Label(text="Cartão de Credito", font=("Century Gothic", 10), bg="White")
LabelCredito.place(x=120, y=250)
ValCredito = Label(text="R$ 255,00", font=("Century Gothic", 20), bg="White")
ValCredito.place(x=350, y=215)

#==== Label Debito ====#
ImgLabel = Label(image=imgDebito, bg="White")
ImgLabel.place(x=50, y=330)
LabelDebito = Label(text="Cartão de Debito", font=("Century Gothic", 10), bg="White")
LabelDebito.place(x=120, y=365)
ValDebito = Label(text="R$ 235,00", font=("Century Gothic", 20), bg="White")
ValDebito.place(x=350, y=330)

#==== Botões ====#
DinheiroButton = ttk.Button(text="Escolher",width=10)
DinheiroButton.place(x=380,y=145)
CreditoButton = ttk.Button(text="Escolher",width=10)
CreditoButton.place(x=380,y=260)
DebitoButton = ttk.Button(text="Escolher",width=10)
DebitoButton.place(x=380,y=375)

#==== Execução ====#
janela.mainloop()