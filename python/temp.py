from tkinter import *
def clicar():
    nome = textentry.get()
    output.delete(0.0, END)
    output.insert(END, f"Oi {nome} fala ae mano ")
window = Tk()
window.title("Comprimentador")
text = Label(window, text="Diga seu nome mermão!!")
text.grid(row=2, column=0, sticky=W)
# Adicionar botao para comprimentar
botao = Button(window, text="Comprimentar", command=clicar)
botao.grid(row=4, column=0, sticky=W)
# Create a text entry box
textentry = Entry(window)
textentry.grid(row=3, column=0, sticky=W)
# Caixa de saída
output = Text(window)
output.grid(row=5, column=0, columnspan=2, sticky=W)
window.mainloop()