#구간 5개로 나눈거 모델링
#구간 4개를 써서 이 모델은 안씀
class xgb_c_model():
    def __init__(self, input, target):
        self.input = input
        self.target = target

    def data_transform(self):
        from sklearn.model_selection import train_test_split
        import xgboost as xgb
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        print(len(train_input))
        dtrain = xgb.DMatrix(data = train_input, label = train_target)
        dtest = xgb.DMatrix(data = test_input, label = test_target)
        return dtrain, dtest
    
    def data_split(self):
        from sklearn.model_selection import train_test_split
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        return train_input, test_input, train_target, test_target
    
    def get_test(self):
        from sklearn.model_selection import train_test_split
        import xgboost as xgb
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        dtrain = xgb.DMatrix(train_input, train_target)
        dtest = xgb.DMatrix(test_input, test_target)
        return dtest
    
    def get_target(self):
        from sklearn.model_selection import train_test_split
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        return test_target

    def train(self):
        from xgboost import XGBClassifier
        from sklearn.model_selection import GridSearchCV
        import numpy as np
        train_input, test_input, train_target, test_target = self.data_split()
        xgbc = XGBClassifier()
        iter1 = np.arange(0.001, 0.01, 0.001)
        x_param = {'n_estimators' : [i for i in range(100, 500, 10)], 'learning_rate' : [j for j in iter1], 'max_depth' : [l for l in range(2, 7)], 'gamma' : [n for n in range(0, 5)], 'colsample_bytree' : [0.8, 0.9]}
        xgb_grid = GridSearchCV(xgbc, param_grid = x_param, scoring = 'accuracy', n_jobs = -1, verbose = 2)
        model = xgb_grid.fit(train_input, train_target)
        print("best parameter : ", model.best_params_)
        print("Accuracy : {}".format(model.best_score_))
        return model
    

    def model_test(self, model):
        import xgboost as xgb
        train_input, test_input, train_target, test_target = self.data_split()
        preds = model.predict(test_input)
        return preds
    
    def get_eval(self, preds):
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
        train_input, test_input, train_target, test_target = self.data_split()
        confusion = confusion_matrix(test_target, preds)
        accuracy = accuracy_score(test_target, preds)
        precision = precision_score(test_target, preds, average = 'weighted')
        recall = recall_score(test_target, preds, average = 'weighted')
        F1 = f1_score(test_target, preds, average = 'weighted')
        print('오차행렬 : \n', confusion)
        print('accuracy : ', accuracy)
        print('정밀도 : ', precision)
        print('재현율 : ', recall)
        print('F1 : ', F1)