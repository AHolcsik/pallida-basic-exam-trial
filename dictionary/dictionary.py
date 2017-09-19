dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

hun_word = "kutya"
eng_word = "dog"

def add_word(hun_word, eng_word):
    entry = {hun_word: eng_word}
    dictionary.append(entry)
    return(dictionary)


# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'

def translate_to_eng(hun_word):
    for element[0] in dictionary.values():
        if element[0] == hun_word:
            print(element[1])



translate_to_eng(hun_word)
add_word(hun_word, eng_word)
print(dictionary)