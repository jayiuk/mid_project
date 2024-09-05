import pandas as pd
import pickle as pkl

data = pd.read_csv('./pitchers_stat_cluster2.csv')
df_input = data[['ERA', 'QS_G', 'SO', 'WAR_x', 'W', 'IP', 'K_BB', 'exp_QS','SO_G', 'QS', 'NP', 'RA_9', '연차', 'TBF', '현재연봉', 'WHIP', 'K-BB', 'NP/IP']]
df_target = data['salary_cluster']



from xgb_classification2 import xgb_c_model
x_model = xgb_c_model(df_input, df_target)
x_model_fin = x_model.train()

dtest = x_model.get_test()
preds = x_model.model_test(x_model_fin)



x_model.get_eval(preds)

name = 'pitcher_salary_predict2.model'
pkl.dump(x_model_fin, open(name, 'wb'))