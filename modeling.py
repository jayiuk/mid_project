import xgboost as xgb
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score

data = pd.read_csv('./modeling_data.csv')

class modeling():
    def __init__(self, data, params):
        self.data = data
        self.params = params

    def split_data(self):
        data = self.data
        y = data['예측연봉']
        x = data.drop(['예측연봉'], axis = 1)
        x_train, x_target, y_train, y_target = train_test_split(x, y, test_size = 0.2, random_state = 42)
        return x_train, x_target, y_train, y_target
    
    def get_DMatrix(self, train_data, test_data, train_label, test_label):
        dtrain = xgb.DMatrix(data = train_data, label = train_label)
        dtest = xgb.DMatrix(data = test_data, label = test_label)
        return dtrain, dtest
    
    def xregression(self, d_train, d_test, num_rounds, e_s_r):
        params = self.params
        xlist = [(d_train, 'train'), (d_test, 'eval')]
        x_model_fin = xgb.train(params = params, dtrain = d_train, num_boost_round = num_rounds, early_stopping_rounds = e_s_r, evals = xlist)
        return x_model_fin