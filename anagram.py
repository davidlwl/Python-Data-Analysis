'''#5 Your challenge today is to write a program that can find the amount
of anagrams within a .txt file. For example, "snap" would
be an anagram of "pans", and "skate" would be an anagram of "stake".'''

import itertools
from PyDictionary import PyDictionary
dictionary=PyDictionary()
from urllib.request import urlopen

while True:
    word = input('what word\n> ').lower()
    scrambled = urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words3.txt').read().split()
    matched = [i.decode("utf-8") for i in scrambled if sorted(word) == sorted(i.decode("utf-8"))]
    print(matched)


'''#using dictionary and permutations, but takes too long
perms = [''.join(perm) for perm in itertools.permutations(word.lower())]
for i in perms:
    try:
        if dictionary.meaning(i) != None:
            print(i)
    except Exception:
        pass'''


