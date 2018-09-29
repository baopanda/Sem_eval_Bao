from pyvi import ViTokenizer

datas = []
with open("StopWord.txt",'r',encoding='utf-8') as f:
    for i in f:
        datas.append(i)

with open("StopWord_seg.txt",'w',encoding='utf-8') as f:
    for i in datas:
        i = ViTokenizer.tokenize(i)
        f.write(i+"\n")