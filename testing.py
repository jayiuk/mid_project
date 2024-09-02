import pandas as pd

data = pd.read_csv('./pitchers_stat_cluster.csv')
df_input = data[['ERA', 'QS_G', 'SO', 'WAR_x', 'W', 'IP', 'K_BB', 'exp_QS','SO_G', 'QS', 'NP', 'RA_9', '연차', 'TBF', '현재연봉', 'WHIP']]
df_target = data['salary_cluster']

parameter = {'max_depth' : 3, 'eta' : 0.009, 'objective' : 'multi:softmax', 'eval_metrics' : 'merror', 'num_class' : 4}

from xgb_classification import xgb_c_model
x_model = xgb_c_model(df_input, df_target)
x_model_fin = x_model.train(parameter, 400, 100)

dtest = x_model.get_test()
preds = x_model.model_test(x_model_fin, dtest)
print(preds)
print(len(preds))
target = x_model.get_target()
target = target.values.tolist()
print(target)
print(len(target))

x_model.get_eval(target, preds)