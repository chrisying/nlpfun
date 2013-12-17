# Basic Natural Language Processing
# ** WORK IN PROGRESS **
# Chris Ying, 2013

import string, random
from Tkinter import *

# Class for storing info on a text
class Book:
    def __init__(self, input):
        if input[-5:-1] == '.txt':  #if reading a plaintext
            self.words = self.readString(open(input[:-1], 'r').read())
        else:   #if reading directly from string
            self.words = self.readString(input)
        self.dict = {}
        if len(self.words) < 1:
            raise Exception('Book too short')
        #self.printWords()
        #print(self.createString(random.randint(5, 10)))

    def readString(self, text): #parses string
        text = text.lower()
        for c in string.punctuation:
            if c != '\'' and c != '-':
                text = text.replace(c, ' ')
        words = text.split()
        return words

    def analyze(self, pre, post):   #sets up graph of consecutive words
        if pre in self.dict:
            sublist = self.dict[pre]
            for word in sublist:
                if word[0] == post:
                    word[1] += 1
                else:
                    sublist.append([post, 1])
        else:
            sublist = []
            sublist.append([post, 1])
            self.dict[pre] = sublist

    def createString(self, length):     #creates a random string
        str = ''
        slen = 0
        w = random.choice(self.words)
        while slen < length:
            str += w + ' '
            slen += 1
            if (w == '.'):
                str = str[:-2]
                break
            w = random.choice(self.dict[w])[0]
        
        return str[0].upper() + str[1:-1] + '.'

    def printWords(self):   #debugging purposes
        for word in self.dict:
            print self.dict[word]

### GUI ###

class NLPGui:
    def __init__(self, parent):
        parent.title("NLP Fun")

        self.frame = Frame(parent)
        self.frame.pack()

        self.title = Label(self.frame, text = 'Instructions: enter a file name (.txt files only) or copy paste\nany text you want into the text box and click Create!')
        self.title.pack()

        self.textframe = LabelFrame(self.frame, text = 'Text')
        self.textframe.pack()
        self.textbox = Text(self.textframe)
        self.textbox.pack()

        self.numframe = LabelFrame(self.frame, text = 'Length')
        self.numframe.pack()
        self.minframe = LabelFrame(self.numframe, text = 'Min')
        self.minframe.pack(side = 'left')
        self.min = Text(self.minframe, height = 1, width = 10)
        self.min.pack()
        self.maxframe = LabelFrame(self.numframe, text = 'Max')
        self.maxframe.pack(side = 'right')
        self.max = Text(self.maxframe, height = 1, width = 10)
        self.max.pack()

        self.button = Button(self.frame, text = 'Create!', command = self.create)
        self.button.pack()

        self.status = StringVar()
        self.status.set('Press Create! to continue')
        self.stat = Label(self.frame, textvariable = self.status)
        self.stat.pack()

        self.outframe = LabelFrame(self.frame, text = 'Output')
        self.outframe.pack()
        self.out = StringVar()
        self.output = Label(self.outframe, textvariable = self.out)
        self.output.pack()

    def create(self):
        b = Book(self.textbox.get(1.0, END))
        for i in range(len(b.words) - 1):
            print i
            self.status.set(str(int(i * 100 / len(b.words))) + "% done")
            b.analyze(b.words[i], b.words[i + 1])  #analyze sets of 2 words
        b.analyze(b.words[-1], '.')   #add period
        self.out.set(b.createString(random.randint(int(self.min.get(1.0, END)), int(self.max.get(1.0, END)))))
        self.status.set('Done')

root = Tk()
app = NLPGui(root)
root.mainloop()