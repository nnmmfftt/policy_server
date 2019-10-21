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
# 数据量小，使用map的方式存储用户model信息


class Model:
    def __init__(self, name):
        try:
            f = open(name,'rb')
        except FileNotFoundError:
            print("model file open error, check the file")
        else:
            model_map = cPickle.load(f)
            size = len(model_map)

    def __findModel(self, userid, model_map):
        model = model_map[userid]
        return model

    def predict(self, userid, test_case):
        model = __findModel__(userid, model_map)
        return model.predict(test_case)

    def __modelGenerator__(self, userid, policy_file):
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

    def __saveModel__(self, name, userid, model):
        # 保存新的user_id对应的model
        # 再将model落盘
        model_map[userid] = model
        save_name = name+'.pkl'
        cPickle.dump(model_map, open(save_name, 'w'), cPickle.HIGHEST_PROTOCOL)

    def drawDecisionTree(self, model, filename_pdf_output):
        # the DT graph
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        # 使用grahpviz绘制决策树图
        dot_data = tree.export_graphviz(model, out_file=None)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf(filename_pdf_output)