import pandas as pd
from os.path import join
from lxml import etree as ET
from pyvi import ViTokenizer
import StopWords

tree = ET.parse(join("data", "rest_final.xml"))
root = tree.getroot()

reviews = root.findall("Review")
sentences = root.findall("**/sentence")
print("# Reviews   : ", len(reviews))
print("# Sentences : ", len(sentences))

datas = []
categories = []
for i in root.iter('sentence'):
    if(i.get('OutOfScope') != 'TRUE'):
        opinion = i.find('Opinion')
        if(opinion.attrib['category'] == 'REST#SERVICE'):
            text = i.find('text')
            datas.append(text.text)
            categories.append(opinion.attrib['category'])
        else:
            text = i.find('text')
            text = text.text
            datas.append(text)
            categories.append('None')

# SPECIAL_CHARACTER = '%@$=+-!;🏻/()👍*❤"😍&^:♥<>#|\n\t\''
# with open("datas_stopword.txt",'w',encoding='utf-8') as file:
#     for i in datas:
#         my_words = i.split(" ")
#         for word1 in i:
#             if word1 in SPECIAL_CHARACTER:
#                 i = i.replace(word1, "")
#                 i = i.replace("  ", " ")
#         for word in my_words:
#             if len(word) > 20 or len(word) < 2:
#                 i = i.replace(word, "")
#                 i = i.replace("  ", " ")
#         i = ViTokenizer.tokenize(i)
#         my_words = i.split(" ")
#         for word in my_words:
#             if word in StopWords.STOP_WORDS:
#                 i = i.replace(word, "")
#                 i = i.replace("  ", " ")
#         i = i.lower()
#         file.write(i+"\n")

with open("labels_SERVICE.txt",'w',encoding='utf-8') as file:
    for i in categories:
        file.write(str(i)+"\n")

print(len(datas))
print(len(categories))
