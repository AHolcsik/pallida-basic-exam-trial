dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

#dictionary["kutya"] = "dog"

hun_word = "alma"
#eng_word = "apple"

# def add_word(hun_word, eng_word):
#     dictionary[hun_word] = eng_word

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


# def translate_to_hun(eng_word):
#     hungarian = ""
#     for p in dictionary:
#         if p["apple"] == eng_word:
#             print(p)


def search("apple"):
    for p in dictionary:
        if p["alma"] == "apple":
            return p

print(search("apple"))    


def translate_to_eng(hun_word):
    pass

# add_word(hun_word, eng_word)
