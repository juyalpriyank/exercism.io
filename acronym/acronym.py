import re

def abbreviate(words):
    acronym = ''
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    words_list = words.split()
    for _index, word in enumerate(words_list):
        if not word.isalpha():
            words = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\:"|<,./<>?]', word)
            words_list.pop(words_list.index(word))
            for _index1, word1 in enumerate(words):
                words_list.insert(_index + _index1, word1)

    for i in words_list:
        if not i == '':
            acronym += i[0].capitalize()

    return acronym




