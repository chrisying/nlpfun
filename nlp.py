# Basic Natural Language Processing
# ** WORK IN PROGRESS **
# Chris Ying, 2013

import string, random

class Book:
	def __init__(self, filename):
		self.words = self.readFile(filename)
		self.dict = {}
		if len(self.words) < 1:
			raise Exception('Book too short')
		for i in range(len(self.words) - 1):
			self.analyze(self.words[i], self.words[i + 1])
		self.analyze(self.words[-1], '.')
		#self.printWords()
		print(self.createString(random.randint(5, 10)))

	def readFile(self, filename):
		f = open(filename, 'r')
		text = f.read()
		text = text.lower()
		for c in string.punctuation:
			text = text.replace(c, ' ')
		words = text.split()
		return words

	def analyze(self, pre, post):
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

	def createString(self, length):
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

	def printWords(self):
		for word in self.dict:
			print self.dict[word]

Book('sherlockp1.txt')
print 'NLP Complete!'
