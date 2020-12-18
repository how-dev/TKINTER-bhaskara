from tkinter import *
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------------- Atribuindo interface -------------------------------------------------
janela = Tk()
janela.title('Howard do 2° Grau')
# --------------------------------------------- Cor da interface -------------------------------------------------------
janela['bg'] = 'pink'
# --------------------------------------------- Função do 2° grau ------------------------------------------------------


def bt():
    if str(ed1.get()).isalpha() is False and str(ed2.get()).isalpha() is False and str(ed3.get()).isalpha() is False:
        lb['text'] = 'Digite um valor numérico para a, b e c: '
        a = float(ed1.get())
        b = float(ed2.get())
        c = float(ed3.get())
        raiz = math.pow(b, 2) - 4 * a * c
        delta['text'] = f'Delta vale: {raiz}'
        if raiz < 0:
            lb['text'] = 'Operação feita com sucesso! OBS: Delta negativo!'
            x1['text'] = 'x1 vale: {:.2f}'.format((-b - cmath.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a))
            x2['text'] = 'x2 vale: {:.2f}'.format((-b + cmath.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a))
            xv['text'] = 'x do vértice: {:.2f}'.format(-b / (2 * a))
            yv['text'] = 'y do vértice: {:.2f}'.format(-(math.pow(b, 2) - 4 * a * c) / (4 * a))
        else:
            lb['text'] = 'Operação feita com sucesso!'
            x1['text'] = 'x1 vale: {:.2f}'.format((-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a))
            x2['text'] = 'x2 vale: {:.2f}'.format((-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a))
            xv['text'] = 'x do vértice: {:.2f}'.format(-b / (2 * a))
            yv['text'] = 'y do vértice: {:.2f}'.format(-(math.pow(b, 2) - 4 * a * c) / (4 * a))
        f = lambda x: a * math.pow(x, 2) + b * x + c

        x = np.array(np.linspace(-80, 80, 200))
        y1 = np.array([f(i) for i in x])

        plt.plot(x, y1)

        plt.title('Parábola')
        plt.grid()
        plt.show()
    else:
        lb['text'] = 'Resultado: Não numérico'


# ------------------------------------------- Espaços para escrever ----------------------------------------------------
ed1 = Entry(janela, bd=2)
ed1.place(x=130, y=70)
ed2 = Entry(janela, bd=2)
ed2.place(x=130, y=95)
ed3 = Entry(janela, bd=2)
ed3.place(x=130, y=120)
# -------------------------------------------- Espaçadores -------------------------------------------------------------
sp1 = Label(janela, text='-------------------', bg='pink')
sp1.place(x=110, y=161)
sp2 = Label(janela, text='-------------------', bg='pink')
sp2.place(x=110, y=185)
sp3 = Label(janela, text='-------------------', bg='pink')
sp3.place(x=110, y=215)
sp4 = Label(janela, text='-------------------', bg='pink')
sp4.place(x=110, y=240)
sp5 = Label(janela, text='-------------------', bg='pink')
sp5.place(x=110, y=267)
# ------------------------------------------- Estrutura visual --------------------------------------------------------
titulo = Label(janela, text='Equação do 2° Grau', bg='purple')
titulo.pack(side=TOP, fill=X)
parede1 = Label(janela, text='', bg='purple')
parede1.pack(side=LEFT, fill=Y)
parede2 = Label(janela, text='', bg='purple')
parede2.pack(side=RIGHT, fill=Y)
al = Label(janela, text='a  = ', bg='pink')
al.place(x=90, y=70)
bl = Label(janela, text='b  = ', bg='pink')
bl.place(x=90, y=90)
cl = Label(janela, text='c  = ', bg='pink')
cl.place(x=90, y=110)
# -------------------------------------- Especificadores ---------------------------------------------------------------
lb2 = Label(janela, text='>>>ax² + bx + c<<< ', bg='pink')
lb2.pack(side=TOP, fill=X)
lb = Label(janela, text='Digite um valor numérico para a, b e c: ', bg='pink')
lb.pack(side=TOP, fill=X)
delta = Label(janela, text='Delta vale: ', bg='pink')
delta.place(x=110, y=150)
x1 = Label(janela, text='x1 vale: ', bg='pink')
x1.place(x=110, y=174)
x2 = Label(janela, text='x2 vale: ', bg='pink')
x2.place(x=110, y=200)
xv = Label(janela, text='x do vértice: ', bg='pink')
xv.place(x=110, y=226)
yv = Label(janela, text='y do vértice: ', bg='pink')
yv.place(x=110, y=252)
# --------------------------------------- Botão Calcular ---------------------------------------------------------------
bt = Button(janela, text='Calcular', width=5, height=8, command=bt, bg='purple', bd=8)
bt.place(x=10, y=90)
# --------------------------- Tamanho, posicionamento e execução da interface ------------------------------------------
janela.geometry('350x300+1400+300')
janela.mainloop()
# ----------------------------------------------------------------------------------------------------------------------
