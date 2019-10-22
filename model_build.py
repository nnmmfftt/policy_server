# -*- coding: utf-8 -*-
__author__ = 'hiqex'
# 为开发使用，系统除了每次在自动更新时条用此文件中函数更新每一个用户的model，管理员能够创建用户，
# 此时系统能够为新用户创建model。

import policy_comp
import _pickle as cPickle
import numpy as np
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import pydotplus
import os
import sys
# 实验使用数据量小，使用dict + file的方式存储用户model信息


class Model:
    def __init__(self, name):
        try:
            f = open(name, 'rb')
        except FileNotFoundError:
            self.model_map = {}
            print("model file open error, check the file")
        else:
            self.model_map = cPickle.load(f)
            self.size = len(self.model_map)

    def __findmodel(self, userid=0):
        model = self.model_map[userid]
        return model

    def predict(self, userid, test_case):
        model = self.__findmodel(userid)
        m = model.predict(test_case)
        return m

    def __model_update(self,request):

        model_map

    def __modelGenerator(self, userid, policy_file):
        # 新用户需要生成policy，以及更新了策略文件后需要重新修改policy文件后需要重新build model
        X = []
        Y = []
        data = pd.read_csv(policy_file, header=None)
        data = data.drop([0, 1, 2, 3], axis=1)
        # The policy have several info useless
        X = data.drop(10, axis=1)
        #  the '10' will be changed, header have been moved.
        Y = data[10]
        # very noob
        # 归一化
        scaler = MinMaxScaler()
        # print(X)
        X = scaler.fit_transform(X)
        X = np.array(X, dtype=np.float32)
        Y = np.array(Y, dtype=np.float32)
        # 交叉分类
        train_X, test_X, train_y, test_y = train_test_split(X,
                                                            Y,
                                                            test_size=0.2)  # test_size:测试集比例20%

        model = tree.DecisionTreeClassifier(criterion='gini')  # gini impurity
        # model = tree.DecisionTreeClassifier(criterion='entropy')    # information gain
        model = model.fit(train_X, train_y)
        return model
        # print(model)

    def __saveModel(self, name, userid, model):
        # 保存新的user_id对应的model
        # 再将model落盘
        self.model_map[userid] = model
        save_name = name+'.pkl'
        cPickle.dump(self.model_map, open(save_name, 'w'), cPickle.HIGHEST_PROTOCOL)

    def drawDecisionTree(self, model, filename_pdf_output):
        # the DT graph
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        # 使用grahpviz绘制决策树图
        dot_data = tree.export_graphviz(model, out_file=None)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf(filename_pdf_output)
