"""
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

# solución
def pig_it(text: str) -> str:
    words = text.split()
    r = []
    
    for word in words:
        if word.isalpha():
            w = f"{word[1:]}{word[0]}ay"
        else:
            w = word
        r.append(w)
    
    return ' '.join(r)


print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !


# otras soluciones

def pig_it(text: str) -> str:
    words = text.split()
    latin_words = []

    for word in words:
        if word.isalpha():
            latin_word = word[1:] + word[0] + 'ay'
        else:
            latin_word = word
        latin_words.append(latin_word)

    return ' '.join(latin_words)


def pig_it(text: str) -> str:
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)
            
    return ' '.join(res)