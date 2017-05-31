'''Create a program that can take a piece of text and encrypt it with an alphabetical substitution cipher.
This can ignore white space, numbers, and symbols.
for extra credit, make it encrypt whitespace, numbers, and symbols!
for extra extra credit, decode someone elses cipher!'''

import string
de = [x for x in string.ascii_lowercase[::-1]]
d = {}
d["'"] = "'"
d["."] = "."
d['/'] = '/'
for idx, i in enumerate(string.ascii_lowercase):
    d[i] = de[idx]

def scramber(x):
    lister = [d[y] for y in x.lower().replace(" ","")]
    return (" ".join(lister).replace(" ","") + " ")
    

while True:
    list_words = []
    word = input('please input word/words to be ciphered\n> ')
    words = [x for x in word.split()]
    if len(words) == 1:
        ds = [d[y] for y in word.lower().replace(" ","")]
        print(" ".join(ds).replace(" ",""))
    else:
        for i in words:
            list_words += [scramber(i)]
        print(" ".join(list_words))
        
'''For this challenge, you need to write a program that will take the scrambled words from this post, and compare them against THIS WORD LIST to unscramble them. For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!
Here are your words to de-scramble:'''

from urllib.request import urlopen

word_list = urlopen('https://pastebin.com/raw/jSD873gL').read().split()

scrambled_words = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle',
                   'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

for scrambled in sorted(scrambled_words, key=len):
    matches = [word.decode("utf-8") for word in word_list if sorted(scrambled) == sorted(word.decode("utf-8"))]
    #separate both unscrakbled and scrambled into ['a', 'a', 'e', 'k', 'm', 'r', 't'], if matches, print.
    print (scrambled + ": " + ' '.join(matches))

