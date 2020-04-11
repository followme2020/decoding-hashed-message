messagefile = open("message.txt", "r")

decripting_key_dic = { 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
dlist = []
new_text = []

def read_text_from_file(path_to_file):
    with open(path_to_file, 'r') as f:
        plain_text = f.read()
        all_words = plain_text.split()
    return all_words

words = read_text_from_file('./message.txt')
print(words)


def decription_of_word (word):
    dlist.clear()
    for letter in word:
        new_letter = decripting_key_dic.get(letter, letter)
        dlist.append(new_letter)
        new_word = ''.join(dlist)
        #coudnt do the decription and scaning in 1 function.
    return (new_word)

for word in words:
    a_word = decription_of_word(word)
    new_text.append(a_word)
print(new_text)


def saving_decoded(str_text, wanted_name):
    decoded_text = wanted_name + '.txt'
    file = open(decoded_text, 'w+')
    file.write(str_text)
    file.close()

str_text = ""
for element in new_text:
    str_text += (element+ ' ')
wanted_name = str(input('please enter new file name:'))
saving_decoded(str_text, wanted_name)
# the_file = open(wanted_name + '.txt')
# print(the_file.read())
# the_file.close()


def sum_check(path_to_or_file, path_to_dec_file):
    count = 0
    all = True
    with open(path_to_or_file, 'r') as f:
        plain_text = f.read()
        all_or_words = plain_text.split()
    with open(path_to_dec_file,"r") as f:
        plain_dec_text = f.read()
        all_dec_words = plain_dec_text.split()
    for item in all_or_words:
        if len(item) == len(all_dec_words[count]):
            temp = True
        else:
            all = False
        count += 1
    return all

check = sum_check("./message.txt", wanted_name +'.txt')
print("The check ended up being:", check)