import string


with open('ascii.txt', 'r') as f:
    contents = f.read()

# words = set(contents.split())
# words = contents.split()


def ceaser_cypher(message):
    LETTERS = string.ascii_uppercase
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in contents:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Key #{}: {}'.format(key, translated))


ceaser_cypher(contents)
