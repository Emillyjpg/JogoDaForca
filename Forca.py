import random
import tkinter as tk

class JogodaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("500x500")
        self.root.config(bg="#0a2139")

        self.palavras = ["python", "java", "kotlin", "javascript", "ruby", "swift"]
        self.secreta = random.choice(self.palavras).lower()
        self.acertos = ["_"] * len(self.secreta)
        self.tentativas = 5
        self.letras_erradas = []

        # Label da palavra
        self.label_palavra = tk.Label(root,
                                      text=" ".join(self.acertos),
                                      font=("Helvetica", 24),
                                      bg="#0a2139",
                                      fg="white")
        self.label_palavra.pack(pady=20)

        # Instrução
        self.label_instrucao = tk.Label(root,
                                        text="Digite uma letra:",
                                        font=("Helvetica", 14),
                                        bg="#0a2139",
                                        fg="White")
        self.label_instrucao.pack(pady=10)

        # Entrada da letra
        self.letra_entry = tk.Entry(root, font=("Helvetica", 18))
        self.letra_entry.pack(pady=10)

        # Botão de adivinhar
        self.botaoAdivinhar = tk.Button(root,
                                        text="Adivinhar",
                                        font=("Helvetica", 14),
                                        command=self.adivinhar,
                                        bg="#27ae60",
                                        fg="white")
        self.botaoAdivinhar.pack(pady=5)

        # Tentativas restantes
        self.label_tentativas = tk.Label(root,
                                         text=f"Tentativas restantes: {self.tentativas}",
                                         font=("Helvetica", 14),
                                         bg="#2c3e50",
                                         fg="white")
        self.label_tentativas.pack(pady=10)

        # Letras erradas
        self.label_erradas = tk.Label(root,
                                      text="Letras erradas: nenhuma",
                                      font=("Helvetica", 14),
                                      bg="#0a2139",
                                      fg="white")
        self.label_erradas.pack()

        # Status
        self.label_status = tk.Label(root,
                                     text="",
                                     font=("Helvetica", 16),
                                     bg="#0a2139",
                                     fg="red")
        self.label_status.pack(pady=10)

    # Método de adivinhar letra
    def adivinhar(self):
        chute = self.letra_entry.get().lower()

        if not chute.isalpha():
            self.label_status.config(text="Por favor, digite APENAS letras.", fg="yellow")
        elif len(chute) == 1:
            if chute in self.acertos or chute in self.letras_erradas:
                self.label_status.config(text="Você já tentou essa letra.", fg="yellow")
            elif chute in self.secreta:
                for i, l in enumerate(self.secreta):
                    if l == chute:
                        self.acertos[i] = chute
                self.label_status.config(text="Letra correta!", fg="green")
            else:
                self.letras_erradas.append(chute)
                self.tentativas -= 1
                self.label_status.config(text="Letra incorreta.", fg="red")
        else:
            if chute == self.secreta:
                self.acertos = list(self.secreta)
                self.label_status.config(text="Parabéns! Você ganhou!", fg="green")
            else:
                self.tentativas -= 1
                self.label_status.config(text="Palavra incorreta.", fg="red")


        self.letra_entry.delete(0, tk.END)
        self.atualizar_interface()

    # Método para atualizar interface
    def atualizar_interface(self):
        self.label_palavra.config(text=" ".join(self.acertos))
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_erradas.config(text="Letras erradas: " + ", ".join(self.letras_erradas) if self.letras_erradas else "Letras erradas: nenhuma")

        if "_" not in self.acertos:
            self.label_status.config(text="Parabéns! Você ganhou!", fg="green")
            self.desabilitar_jogo()
        elif self.tentativas == 0:
            self.label_status.config(text=f"Você perdeu! A palavra era: {self.secreta}", fg="red")
            self.desabilitar_jogo()

    # Método para desabilitar jogo
    def desabilitar_jogo(self):
        self.letra_entry.config(state="disabled")
        self.botaoAdivinhar.config(state="disabled")


# Rodar o jogo
root = tk.Tk()
jogo = JogodaForca(root)
root.mainloop()
