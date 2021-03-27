from googletrans import Translator

trans = Translator()
print('please enter word: ')
word = str(input())
out_trans = trans.translate(word, dest='de')
print(out_trans.text)