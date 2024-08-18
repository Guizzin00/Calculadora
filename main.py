import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        
        self.entrada = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.criar_botoes()
        
    def criar_botoes(self):
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        linha = 1
        coluna = 0
        for texto in botoes:
            acao = lambda x=texto: self.pressionar(x)
            tk.Button(self.root, text=texto, font=("Arial", 18), width=4, height=2, command=acao).grid(row=linha, column=coluna, padx=5, pady=5)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

    def pressionar(self, tecla):
        if tecla == 'C':
            self.entrada.delete(0, tk.END)
        elif tecla == '=':
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))
            except Exception as e:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Erro")
        else:
            self.entrada.insert(tk.END, tecla)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
