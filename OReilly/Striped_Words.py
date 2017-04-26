import string

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = string.punctuation

def checkio(text):
    text = text.upper()

    for c in VOWELS:
        text = text.replace(c, 'v')

    for c in CONSONANTS:
        text = text.replace(c, 'c')

    for c in PUNCTUATION:
        text = text.replace(c, ' ')

    count = 0
    for word in text.split():
        if len(word) > 1 and word.isalpha():
            if word.find('cc') == -1 and word.find('vv') == -1:
                count += 1

    return count

if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
