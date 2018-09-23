import pandas as pd
from os.path import join
from lxml import etree as ET
from pyvi import ViTokenizer
from Sem_eval_Bao import StopWords

tree = ET.parse(join("data_valid", "data_valid_new.xml"))
root = tree.getroot()

reviews = root.findall("Review")
sentences = root.findall("**/sentence")
print("# Reviews   : ", len(reviews))
print("# Sentences : ", len(sentences))
count = 0
# count_1 = 0
datas = []
categories = []
for i in root.iter('sentence'):
    # count_1+=1
    # print("la: " + str(count_1))
    if(i.get('OutOfScope') != 'TRUE'):

        opinion = i.find('Opinion')

        if(opinion.attrib['category'] == 'REST#STYLEOPTIONS'):
            text = i.find('text')
            datas.append(text.text)
            categories.append(opinion.attrib['category'])
        else:
            text = i.find('text')
            text = text.text
            datas.append(text)
            categories.append('None')

SPECIAL_CHARACTER = '%@$=+-!;🏻/()👍*❤"😍&^:♥<>#|\n\t\''
with open(join("data_valid", "datas_STYLEOPTIONS_valid.txt"),'w',encoding='utf-8') as file:
    for i in datas:
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
        # my_words = i.split(" ")
        # for word in my_words:
        #     if word in StopWords.STOP_WORDS:
        #         i = i.replace(word, "")
        #         i = i.replace("  ", " ")
        i = i.lower()
        file.write(i+"\n")

with open(join("data_valid", "labels_STYLEOPTIONS_valid.txt"),'w',encoding='utf-8') as file:
    for i in categories:
        file.write(str(i)+"\n")

print(len(datas))
print(len(categories))
