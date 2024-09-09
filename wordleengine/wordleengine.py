import sys
import string
class WordleEngine():
    def load_list(self, filename, interval):
        try:
            with open(filename, 'r') as f:
                text = f.read()
            text = list(text.split(interval))
            return text
        except Exception as s:
            print(f'cannot operate on file: {s}')
            sys.exit(1)



    def __init__(self):
        self.answerlist = self.load_list('answer.txt', '\n')
        self.reset()
        
        self.alphabet = string.ascii_lowercase
        self.first = []
        self.second = []
        self.third = []
        self.fourth = []
        self.fifth = []

        self.firstL = {}
        self.secondL = {}
        self.thirdL = {}
        self.fourthL = {}
        self.fifthL = {} 
        
        self.clue = []
        self.keyword = []

    def reset(self):
        try:
            self.wordlist = self.load_list('valid_wordle_words.txt', '\n')
        except Exception as s:
            print(f'cannot load list: {s}')
            sys.exit(1)
            

    def prune(self):
        try:
            keywordbyletter = list(self.keyword)
        except Exception as s:
            print(f'issue with keyword: {s}')
            sys.exit(1)
        delete = []
        
        try:
            for word in self.wordlist:
                
                wordbyletter = list(word)

                for index, value in enumerate(self.clue):
                    if value == 'g':
                        if not wordbyletter[index] == keywordbyletter[index]:
                            try:
                                delete.append(word)
                            except ValueError:
                                pass
                    
                    elif value == 'y':
                        if wordbyletter[index] == keywordbyletter[index] or not keywordbyletter[index] in word:
                            try:
                                delete.append(word)
                            except ValueError:
                                pass

                    elif value == 'b':
                        if wordbyletter[index] == keywordbyletter[index] or keywordbyletter[index] in word:
                            try:
                                delete.append(word)
                            except ValueError:
                                pass
            delete.append(self.keyword)

            for word in delete:
                try:
                    self.wordlist.remove(word)
                except ValueError:
                    pass        
        except Exception as s:
            print(f'problem during list pruning: {s}')
            sys.exit(1)

    def addall(self):
        try:
            for word in self.wordlist:
                wordbyletter = list(word)
                self.first.append(wordbyletter[0])
                self.second.append(wordbyletter[1])
                self.third.append(wordbyletter[2])
                self.fourth.append(wordbyletter[3])
                self.fifth.append(wordbyletter[4])
        except Exception as s:
            print(f'problem during evaluation: {s}')
            sys.exit(1)

    def countall(self):
        try:
            for letter in self.alphabet:
                self.firstL[letter] = self.first.count(letter)
                self.secondL[letter] = self.second.count(letter)
                self.thirdL[letter] = self.third.count(letter)
                self.fourthL[letter] = self.fourth.count(letter)
                self.fifthL[letter] = self.fifth.count(letter)
        except Exception as s:
            print(f'problem during counting: {s}')
            sys.exit(1)

    def eval(self):    

        best = ''
        bestpts = 0
        try:
            for word in self.wordlist:
                pts = 0
                wordbyletter = list(word)
                for i in self.alphabet:
                    occurences = wordbyletter.count(i)
                    average = ((self.firstL[i] + self.secondL[i] + self.thirdL[i] + self.fourthL[i] + self.fifthL[i])/5)
                    if occurences > 1:
                        pts -= (occurences * average)
                try:
                    pts += self.firstL[wordbyletter[0]]
                    pts += self.secondL[wordbyletter[1]]
                    pts += self.thirdL[wordbyletter[2]]
                    pts += self.fourthL[wordbyletter[3]]
                    pts += self.fifthL[wordbyletter[4]]
                except:
                    pass
                if pts > bestpts:
                    bestpts = pts
                    best = word
            self.keyword = best
        except Exception as s:
            print(f'problem during evaluation: {s}')
            sys.exit(1)
            
    #this is for running trials
    def check(self, answer):
        self.clue = []
        wordbyletter = list(self.keyword)
        answerbyletter = list(answer)
        for index, value in enumerate(wordbyletter):
            if value == answerbyletter[index]:
                self.clue.append('g')

            elif not value == answerbyletter[index] and value in answer:
                self.clue.append('y')

            else:
                self.clue.append('b')



    def prompt(self, keywordpromptflag):
        try:
            if keywordpromptflag == 1:
                try:
                    self.keyword = str(input('word: ')).lower()

                    if len(self.keyword) != 5:
                        print('That is not a 5 letter word. Please enter a 5 letter word')
                        self.prompt(keywordpromptflag)

                    if not self.keyword in self.wordlist:
                        print('That is not a valid wordle word. Please enter a valid wordle word')
                        self.prompt(keywordpromptflag)
                    keywordpromptflag = 0
                except Exception:
                    print('please enter a valid word')
                    self.prompt(keywordpromptflag)

            try:
                self.clue = list(str(input('colors: ')).lower())

                if len(self.clue) != 5:
                    print('There needs to be 5 colors. Please enter a combination of 5 colors')
                    self.prompt(keywordpromptflag)
                    
                if not all(i in ['g', 'y', 'b'] for i in self.clue):
                    print('Your color sequence must consist of b, y, or g. Please enter a correct combination.')
                    self.prompt(keywordpromptflag)

            except Exception:
                print('please enter a valid combination of colors')
                self.prompt(keywordpromptflag)


        except KeyboardInterrupt:
            sys.exit()

    def iteration(self):
        self.prune()
        self.addall()
        self.countall()
        self.eval()

    # main
    def solve(self):
        try:
            self.prompt(1)

            for i in range(0, 6):
                self.iteration()
                if len(self.keyword) != 5:
                    sys.exit()
                print(self.keyword)
                self.prompt(0)
            sys.exit()
        except:
            sys.exit()



engine = WordleEngine()

engine.solve()