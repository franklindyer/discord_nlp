import markovify
import sys

f = open('corpus/marx.txt', 'r')
TEXT_MODEL = markovify.Text(f, state_size=int(sys.argv[1]))
for i in range(5):
    print(TEXT_MODEL.make_sentence(tries=100))
