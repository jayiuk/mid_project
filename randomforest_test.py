from random_forest import forest_classification
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('./pitchers_stat_cluster.csv')
df_input = data[['ERA', 'QS_G', 'SO', 'WAR_x', 'W', 'IP', 'WHIP','RA_9', 'current_cluster']]
df_target = data['salary_cluster']
fc = forest_classification(df_input, df_target)
train_input, test_input, train_target, test_target = train_test_split(df_input, df_target, test_size = 0.2, random_state = 42)

para = {'n_estimators' : [i for i in range(10, 30, 1)], 'max_depth' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'min_samples_split' : [0.001, 0.01, 0.02, 0.03, 0.1]}

rf_model = fc.modeling_rfclf(para)
preds = fc.model_test(rf_model, test_input)
con_preds = fc.get_score(rf_model, test_input, test_target)