dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'
hun_word = ""

def add_word(hun_word):
    for element in dictionary:
        for i in element:
            hun_word += str([i])
    return(hun_word)

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    pass


def translate_to_eng(hun_word):
    pass

print(add_word(hun_word))