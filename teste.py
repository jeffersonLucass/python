import tkinter as tk
import random

class SimpleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Básico")
        
        self.label = tk.Label(root, text="Clique no botão para jogar!", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Jogar", command=self.play_game, font=("Helvetica", 16))
        self.button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
    
    def play_game(self):
        result = random.choice(["Você ganhou!", "Você perdeu!", "Empate!"])
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    game = SimpleGame(root)
    root.mainloop()