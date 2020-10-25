import markovify

TEXT_MODEL = markovify.NewlineText(open('discord_dump.txt','r'))
print(TEXT_MODEL)
print(TEXT_MODEL.make_sentence_with_start("he",tries=100))
for t in TEXT_MODEL.chain.model:
    if t[0] == 'can only': print(t)
## print(TEXT_MODEL.chain.model[('___BEGIN__','marx')])
## print(TEXT_MODEL.make_sentence_with_start("hegel was a", tries=100))
