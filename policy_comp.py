# -*- coding: utf-8 -*-
__author__ = 'hiqex'
import numpy as np
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import sys


def pred_max(filename, filename_pdf_output):
    # desition tree versio for attr.
    # The policy_sets will have labels
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    X = []
    Y = []
    data = pd.read_csv(filename, header=None)
    data = data.drop([0, 1, 2, 3], axis=1)
    # The policy have several info useless
    X = data.drop(10, axis=1)
    #  the '10' will be changed, header have been moved.
    Y = data[10]
    # very noob
    #归一化
    scaler = MinMaxScaler()
    #print(X)
    X = scaler.fit_transform(X)
    X = np.array(X, dtype = np.float32)
    Y = np.array(Y, dtype = np.float32)
    # 交叉分类
    train_X, test_X, train_y, test_y = train_test_split(X,
                                                       Y,
                                                       test_size=0.2) # test_size:测试集比例20%

    model = tree.DecisionTreeClassifier(criterion='gini')       # gini impurity
    # model = tree.DecisionTreeClassifier(criterion='entropy')    # information gain
    model = model.fit(train_X, train_y)
    # print(model)

    expected = test_y
    predicted = model.predict(test_X)
    print(metrics.classification_report(expected, predicted))       # 输出分类信息
    label = list(set(Y))
    # 去重复，得到标签类别
    print(metrics.confusion_matrix(expected, predicted, labels=label))  # 输出混淆矩阵信息
    # test_DecisionTreeRegressor(train_X, test_X, train_y, test_y)


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # using
    # python policy_comp.py input_file output_file
    pred_max(input_file, output_file)
    # pred_max('../data/dat.csv','../result/DTgraph.pdf')




