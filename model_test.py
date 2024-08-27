import xgboost as xgb
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score
from modeling import modeling

data = pd.read_csv('./modeling_data.csv')
params = {'booster' : 'gblinear', 'feature_selector' : 'shuffle','eta' : 0.05, 'lambda' : 1,'objective' : 'reg:linear', 'eval_metric' : 'mae', 'gamma' : 2}

get_model = modeling(data, params)

x_train, x_target, y_train, y_target = get_model.split_data()

dtrain, dtest = get_model.get_DMatrix(x_train, x_target, y_train, y_target)

xr = get_model.xregression(dtrain, dtest, 400, 20)

