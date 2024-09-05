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

    
    def train(self, parameter, num, early):
        import xgboost as xgb
        dtrain, dtest = self.data_transform()
        model = xgb.train(params = parameter, dtrain = dtrain, num_boost_round = num, early_stopping_rounds = early, evals = [(dtrain, 'train'), (dtest, 'eval')])
        return model
    
    def feature_importance(self, model):
        import xgboost as xgb
        fi = model.feature_importances_
        return fi
    
    def model_test(self, model, test_dmatrix):
        import xgboost as xgb
        preds = model.predict(test_dmatrix)
        return preds
    
    def get_eval(self, test, preds):
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
        confusion = confusion_matrix(test, preds)
        accuracy = accuracy_score(test, preds)
        precision = precision_score(test, preds, average = 'weighted')
        recall = recall_score(test, preds, average = 'weighted')
        F1 = f1_score(test, preds, average = 'weighted')
        print('오차행렬 : \n', confusion)
        print('accuracy : ', accuracy)
        print('정밀도 : ', precision)
        print('재현율 : ', recall)
        print('F1 : ', F1)