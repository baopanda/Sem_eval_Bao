import pickle
from os.path import join

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix


def LoadData(path_data,path_label):
    datas = []
    labels = []
    with open(path_data, 'r', encoding='utf-8')as file:
        for i in file:
            datas.append(i)

    with open(path_label, 'r', encoding='utf-8')as file:
        for i in file:
            labels.append(i)
    return datas, labels

def Classification():
    s = "Kim_chi gọi thêm 10k/bát khá đầy_đặn , ăn giòn vừa cay vừa ."
    pre = []
    pre.append(s)
    datas_valid = []
    labels_valid = []
    # vectorizer = CountVectorizer()
    # transformed_x_valid = vectorizer.fit_transform(s).toarray()
    load_file = open(join("models","STYLEOPTIONS.pkl"),'rb')
    clf = pickle.load(load_file)
    print("Loading file : ",clf)

    with open(join("data_valid", "datas_STYLEOPTIONS_valid.txt"), 'r', encoding='utf-8')as file:
        for i in file:
            datas_valid.append(i)
    with open(join("data_valid", "labels_STYLEOPTIONS_valid.txt"), 'r', encoding='utf-8')as file:
        for i in file:
            labels_valid.append(i)

    X_valid = datas_valid
    a = clf.predict(X_valid)
    with open("predict.txt",'w',encoding='utf-8') as f:
        for i in a:
            f.write(i)
    t = clf.predict(pre)
    print(t)
    # print(a)
    print(confusion_matrix(labels_valid, a))

    # X_train, y_train = LoadData("../data_train/.txt", "labels_new1.txt")

if __name__ == "__main__":
    Classification()

