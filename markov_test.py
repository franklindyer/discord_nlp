import markovify

TEXT_MODEL = markovify.NewlineText(open('discord_dump.txt','r'))
print(TEXT_MODEL)
print(TEXT_MODEL.make_sentence(tries=100))
