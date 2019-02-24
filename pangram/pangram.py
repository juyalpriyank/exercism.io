alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_pangram(sentence):
    try:
        alpha = []
        sentence_alphas = []

        [alpha.append(i) for alphabet in (sentence.lower().split()) for i in alphabet if i not in alpha]

        [sentence_alphas.append(item) for item in alpha if item in alphabets]

        sentence_alphas.sort()
        if sentence_alphas == alphabets:
            return True
        return False

    except Exception as e:
        raise Exception(e.__str__())
