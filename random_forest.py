class forest_classification():
    def __init__(self, input, target):
        self.input = input
        self.target = target

    def get_data(self):
        from sklearn.model_selection import train_test_split
        input = self.input
        target = self.target
        train_input, test_input, train_target, test_target = train_test_split(input, target, test_size = 0.2, random_state = 42)
        return train_input, test_input, train_target, test_target
    
    def modeling_rfclf(self, param):
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import GridSearchCV
        rfclf = RandomForestClassifier()
        train_input, test_input, train_target, test_target = self.get_data()
        grid_forest = GridSearchCV(rfclf, param_grid=param, cv = 3, refit = True)
        grid_forest = grid_forest.fit(train_input, train_target)
        print('GridSearchCV 최적 파라미터:', grid_forest.best_params_)
        print('GridSearchCV 최고 정확도: {0:.4f}'.format(grid_forest.best_score_))
        estimator = grid_forest.best_estimator_
        return estimator

    def model_test(self, model, test_input):
        from sklearn.metrics import accuracy_score
        pred = model.predict(test_input)
        print(pred)
        return pred
    
    def get_score(self, model, test_input, test_target):
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
        pred = model.predict(test_input)
        confusion = confusion_matrix(test_target, pred)
        accuracy = accuracy_score(test_target, pred)
        precision = precision_score(test_target, pred, average = 'weighted')
        recall = recall_score(test_target, pred, average = 'weighted')
        f1 = f1_score(test_target, pred, average = 'weighted')
        print(confusion)
        print('accuracy : ', accuracy)
        print('precision : ', precision)
        print('recall : ', recall)
        print('F1 : ', f1)
        return confusion, accuracy, precision, recall, f1
