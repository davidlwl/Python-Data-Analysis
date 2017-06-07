'''#Write a program that will take a string ("I LIEK CHOCOLATE MILK"),
and allow the user to scan a text file for strings that match. after this,
allow them to replaces all instances of the string with another (
"I quite enjoy chocolate milk. hrmmm. yes.")'''


def scanner():
    line = input('write a string to match \n> ')
    with open('texter.txt', 'r') as f:
        doc = f.read()
        if line in doc:
            rep = input('what would you like to replace it with?')
            doc = doc.replace(line, rep)
        else:
            print('not in file.')
    with open('texter.txt', 'w') as f:
        f.write(doc)
        
scanner()
