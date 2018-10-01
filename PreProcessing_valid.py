from pyvi import ViTokenizer

from Sem_eval_Bao import StopWord1


def PreProcessing(i):
    SPECIAL_CHARACTER = '%@$=+-!;🏻/()👍*❤"😍&^:♥<>#|\n\t\''
    my_words = i.split(" ")
    for word1 in i:
        if word1 in SPECIAL_CHARACTER:
            i = i.replace(word1, "")
            i = i.replace("  ", " ")
    for word in my_words:
        if len(word) > 20 or len(word) < 2:
            i = i.replace(word, "")
            i = i.replace("  ", " ")
    i = ViTokenizer.tokenize(i)
    my_words = i.split(" ")
    for word in my_words:
        if word in StopWord1.STOP_WORDS:
            i = i.replace(word, "")
            i = i.replace("  ", " ")
    i = i.lower()
    return i
