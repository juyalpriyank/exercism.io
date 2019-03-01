def abbreviate(words):
    print(words)
    acronym = ''
    for word in words.split():
        print(word)
        if word[0].isalpha():
            acronym += word[0].capitalize()
        else:
            try:
                acronym += word[1].capitalize()
            except IndexError:
                pass
        print acronym
    return acronym

