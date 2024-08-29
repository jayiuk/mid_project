class regression_model():
    def __init__(self, df):
        self.df = df
    
    def data_split(self):
        import numpy as np
        from sklearn.model_selection import train_test_split
        data = self.df
        X = data[['ERA', 'W', '연차', 'WAR_x', 'Adj_ERA', 'WHIP', 'SO_G', 'pFIP','QS_G', 'WAR_won', 'K_BB','현재연봉']].to_numpy()
        y = data['예측연봉'].to_numpy()
        train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 42)
        return train_x, test_x, train_y, test_y
    
    def scaling(self):
        import numpy as np
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.model_selection import train_test_split
        train_x, test_x, train_y, test_y = self.data_split()
        mm = MinMaxScaler()
        m = mm.fit(train_x)
        scaled_train = m.transform(train_x)
        scaled_test = m.transform(test_x)
        return scaled_train, scaled_test
    
    def modeling(self):
        from sklearn.linear_model import LinearRegression
        import numpy as np
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.model_selection import train_test_split
        train_x, test_x, train_y, test_y = self.data_split()
        scaled_train, scaled_test = self.scaling()

        multi_lr = LinearRegression()
        multi_lr = multi_lr.fit(scaled_train, train_y)
        score = multi_lr.score(scaled_test, test_y)
        print("모델 평가 점수 : ", score)
        return multi_lr, score
