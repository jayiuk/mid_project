class xgb_model():
    def __init__(self, input, target):
        self.input = input
        self.target = target

    def data_transform(self):
        from sklearn.model_selection import train_test_split
        import xgboost as xgb
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        dtrain = xgb.DMatrix(train_input, train_target)
        dtest = xgb.DMatrix(test_input, test_target)
        return dtrain, dtest
    
    def train(self, parameter, num, early):
        import xgboost as xgb
        dtrain, dtest = self.data_transform()
        model = xgb.train(params = parameter, dtrain = dtrain, num_boost_round = num, early_stopping_rounds = early, evals = [(dtrain, 'train'), (dtest, 'eval')])
        return model
    def model_test(self, model, test_dmatrix):
        import xgboost as xgb
        preds = model.predict(test_dmatrix)
        return preds
