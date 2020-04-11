messagefile = open("message.txt", "r")


def read_text_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        plain_text = f.read()
        all_words = plain_text.split()
        print(all_words)
        print(type(all_words))

    return all_words

words = read_text_from_file('./message.txt')
print(words)
decripting_key_dic = { 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
dlist = []
new_text = []

def decription_of_word (word):
    dlist.clear()
    for letter in word:
        new_letter = decripting_key_dic.get(letter, letter)
        dlist.append(new_letter)
        new_word = ''.join(dlist)
    return (new_word)

for word in words:
    a_word = decription_of_word(word)
    new_text.append(a_word)
print(new_text)
