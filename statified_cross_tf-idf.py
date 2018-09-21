from lxml import etree as ET
from os.path import join
import pandas as pd
from sklearn import model_selection
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

datas = []
categories = []

# tree = ET.parse(join("data", "rest_final_new.xml"))
# root = tree.getroot()
#
# reviews = root.findall("Review")
# sentences = root.findall("**/sentence")
# print("# Reviews   : ", len(reviews))
# print("# Sentences : ", len(sentences))
#
# count = 0
# count1 = 0
# for i in root.iter('sentence'):
#     # print("la: " + str(count_1))
#     if (i.get('OutOfScope') != 'TRUE'):
#
#         opinion = i.find('Opinion')
#
#         if (opinion.attrib['category'] == 'REST#LOCATION'):
#             text = i.find('text')
#             datas.append(text.text)
#             categories.append(opinion.attrib['category'])
#             count += 1
# for i in root.iter('sentence'):
#     # print("la: " + str(count_1))
#     if (i.get('OutOfScope') != 'TRUE' and count1 < count+40):
#
#         opinion = i.find('Opinion')
#
#         if (opinion.attrib['category'] != 'REST#LOCATION'):
#             text = i.find('text')
#             text = text.text
#             datas.append(text)
#             categories.append('None')
#             count1 +=1

with open(join("data_new", "datas_QUALITY.txt"),'r', encoding='utf-8')as file:
    for i in file:
        datas.append(i)

with open(join("data_new", "labels_QUALITY.txt"),'r', encoding='utf-8')as file:
    for i in file:
        categories.append(i)


df = pd.DataFrame({"datas": datas, "categories": categories})
data = df['datas']
label = df['categories']
cv_scores = []

skf = StratifiedKFold(label, n_folds=10,shuffle=True,random_state=50)
for train_index, test_index in skf:
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_valid = data[train_index], data[test_index]
    y_train, y_valid = label[train_index], label[test_index]
    vectorizer = CountVectorizer()
    transformed_x_train = vectorizer.fit_transform(X_train)
    # print(transformed_x_train.shape)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(transformed_x_train)
    # print(X_train_tfidf.shape)

    text_clf = Pipeline([('tfidf', TfidfTransformer()),
                         ('clf', MultinomialNB()), ])

    text_clf_svm = Pipeline([('tfidf', TfidfTransformer()),
                             ('clf-svm', SVC(kernel = 'linear')) ])

    text_clf_svm.fit(transformed_x_train, y_train)

    X_valid_transform = vectorizer.transform(X_valid)
    X_valid_tfidf = tfidf_transformer.transform(X_valid_transform)
    y_pred = text_clf_svm.predict(X_valid_tfidf)
    print('Training size = %d, accuracy = %.2f%%' % \
          (len(X_train), accuracy_score(y_valid, y_pred) * 100))
    # print(classification_report(y_valid, y_pred))
    print(confusion_matrix(y_valid, y_pred))
    cv_scores.append(accuracy_score(y_valid, y_pred))
    # print(cv_scores)

print("CV scores: ", cv_scores)
print("mean: : {}".format(np.mean(cv_scores)))



