import random
import tkinter as tk
import tkinter.messagebox
from tkinter.font import Font

class Wordle:
    def __init__(self, word_file):
        self.root = tk.Tk()
        self.root.title('Wordle')
        self.frame = tk.Frame(self.root, width=200, height=200)
        self.frame.bind('<KeyPress>', self.keyPress)

        self.FONT1=Font(family='Lucida Sans', size=48)
        self.load_word(word_file)

    def keyPress(self,event):
        print("Key pressed:", event, event.keysym)

        if event.keysym=='Escape':
            self.root.quit()
        elif event.keysym in ['0', 'Home', 'F5']:
            self.new_game()
        elif event.keysym in ['Return']:
            self.process_guess()
        elif event.keysym in 'abcdefghijklmnopqrstuvwxyz':
            self.add_letter(event.keysym.upper())
        elif event.keysym == 'BackSpace':
            self.do_backspace()
        elif event.keysym == 'F3':
            tk.messagebox.showinfo('Answer', self.word)
            

    def load_word(self,fname):
        with open(fname, 'r') as f:
            self.words = list(map(str.strip, f.read().split('\n')))

    def new_game(self):
        self.board=[]
        self.nGuess=0
        self.guess=''
        self.word = random.choice(self.words)
        print('words:', len(self.words))
        for i in range(6):
            self.board.append([])
            for j in range(5):
                L = tk.Label(self.frame, anchor='center', text=' ')
                L.grid(row=i, column=j, sticky='nsew', padx=5, pady=5)
                L.config(width=2, font=self.FONT1, fg='#ffffff', bg='#939598', borderwidth=5, relief='flat')
                self.board[i].append(L)


    def validate(self):
        print('Validate:', self.guess, self.guess in self.words)
        return self.guess in self.words

    def add_letter(self, key):
        if len(self.guess)<5:
            self.board[self.nGuess][len(self.guess)].config(text=key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess)>0:
            self.guess = self.guess[0:-1]
            self.board[self.nGuess][len(self.guess)].config(text=' ')

    def process_guess(self):
        if not self.validate():
            print('Invalid word:', self.guess)
            for i in range(5):
                self.do_backspace()
        else:
            for j in range(len(self.guess)):
                if self.guess[j]==self.word[j]:
                    self.board[self.nGuess][j].config(fg='#6aaa64')
                elif self.guess[j] in self.word:
                    self.board[self.nGuess][j].config(fg='#c9b458')

            self.nGuess +=1
            self.guess =''
            print('nGuess:', self.nGuess)

        if self.nGuess==6 or self.word==self.guess:
            tk.messagebox.showinfo('Answer', self.word)

    def run(self):
        self.frame.focus_set()
        self.frame.pack()

        self.new_game()
        self.root.mainloop()


def main():
    wd = Wordle('5word.txt')
    wd.run()

if __name__=='__main__':
    main()
