import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from pymongo import MongoClient


class Regression:
    myclient = MongoClient('localhost', 27017)

    data = pd.read_csv("houses_train.csv")
    test_data = pd.read_csv("test.csv")

    def preprocessing(self):
        df = Regression.data
        df = df.set_index('Unnamed: 0')

        def check(col):
            for i in col:
                if not (isinstance(i, float) or (isinstance(i, int))):
                    raise TypeError('The type of variables must be integers')

        if check(df['ceiling_height']) != TypeError:
            fill_ceiling_height = round(df.loc[:, "ceiling_height"].mean())
            df[['ceiling_height']] = df[['ceiling_height']].fillna(fill_ceiling_height)

        if check(df['floor']) != TypeError:
            fill_floor = round(df.loc[:, "floor"].mean())
            df[['floor']] = df[['floor']].fillna(fill_floor)

        if check(df['num_bathrooms']) != TypeError:
            fill_num_bathrooms = round(df.loc[:, "num_bathrooms"].mean())
            df[['num_bathrooms']] = df[['num_bathrooms']].fillna(fill_num_bathrooms)

        if check(df['area']) != TypeError:
            fill_area = round(df.loc[:, "area"].mean())
            df[['area']] = df[['area']].fillna(fill_area)

        if check(df['num_rooms']) != TypeError:
            fill_num_rooms = round(df.loc[:, "num_rooms"].mean())
            df[['num_rooms']] = df[['num_rooms']].fillna(fill_num_rooms)

        if check(df['max_floor']) != TypeError:
            fill_max_floor = round(df.loc[:, "max_floor"].mean())
            df[['max_floor']] = df[['max_floor']].fillna(fill_max_floor)

        if check(df['price']) != TypeError:
            fill_price = round(df.loc[:, "price"].mean())
            df[['price']] = df[['price']].fillna(fill_price)

        # 1 condition-expand
        status = pd.get_dummies(df['condition'], drop_first=True)
        df = pd.concat([df, status], axis=1)
        df.drop(['condition'], axis=1, inplace=True)

        # 2 district-expand
        status = pd.get_dummies(df['district'], drop_first=True)
        df = pd.concat([df, status], axis=1)
        df.drop(['district'], axis=1, inplace=True)

        # 3 building_type-expand
        status = pd.get_dummies(df['building_type'], drop_first=True)
        df = pd.concat([df, status], axis=1)
        df.drop(['building_type'], axis=1, inplace=True)

        pd.set_option('display.max_columns', None)

        self.df = df
        return self.df



    def fit(self):
        X = self.df[['num_rooms', 'area', 'num_bathrooms',
                'ceiling_height', 'newly repaired', 'zero condition', 'Arabkir', 'Center', 'Davtashen',
                'Norq Marash', 'Qanaqer-Zeytun',
                'other', 'panel', 'stone']]

        y = self.df['price']  # Target variable

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% / 30% test
        reg = LinearRegression().fit(X, y)
        reg = reg.fit(X_train, y_train)
        self.X_test = X_test
        self.X_train = X_train
        self.y_train = y_train
        self.y_test = y_test
        self.reg = reg
        return self.reg


    def predict(self):
        y_pred = self.reg.predict(self.X_test)
        #reg.score(X, y)
        pred_price = self.reg.predict(self.X_test)
        self.X_test = self.X_test.assign(Predicted_PRICE=list(pred_price))
        self.pred_price = pred_price
        self.X_test = self.X_test.reset_index()
        return self.X_test

    def test_preprocessing(self):
        test_data = Regression.test_data
        test_data = test_data.set_index('Unnamed: 0')

        def check(col):
            for i in col:
                if not (isinstance(i, float) or (isinstance(i, int))):
                    raise TypeError('The type of variables must be integers')

        if check(test_data['ceiling_height']) != TypeError:
            fill_ceiling_height = round(test_data.loc[:, "ceiling_height"].mean())
            test_data[['ceiling_height']] = test_data[['ceiling_height']].fillna(fill_ceiling_height)

        if check(test_data['floor']) != TypeError:
            fill_floor = round(test_data.loc[:, "floor"].mean())
            test_data[['floor']] = test_data[['floor']].fillna(fill_floor)

        if check(test_data['num_bathrooms']) != TypeError:
            fill_num_bathrooms = round(test_data.loc[:, "num_bathrooms"].mean())
            test_data[['num_bathrooms']] = test_data[['num_bathrooms']].fillna(fill_num_bathrooms)

        if check(test_data['area']) != TypeError:
            fill_area = round(test_data.loc[:, "area"].mean())
            test_data[['area']] = test_data[['area']].fillna(fill_area)

        if check(test_data['num_rooms']) != TypeError:
            fill_num_rooms = round(test_data.loc[:, "num_rooms"].mean())
            test_data[['num_rooms']] = test_data[['num_rooms']].fillna(fill_num_rooms)

        if check(test_data['max_floor']) != TypeError:
            fill_max_floor = round(test_data.loc[:, "max_floor"].mean())
            test_data[['max_floor']] = test_data[['max_floor']].fillna(fill_max_floor)

        # 1 condition-expand
        status = pd.get_dummies(test_data['condition'], drop_first=True)
        test_data = pd.concat([test_data, status], axis=1)
        test_data.drop(['condition'], axis=1, inplace=True)

        # 2 district-expand
        status = pd.get_dummies(test_data['district'], drop_first=True)
        test_data = pd.concat([test_data, status], axis=1)
        test_data.drop(['district'], axis=1, inplace=True)

        # 3 building_type-expand
        status = pd.get_dummies(test_data['building_type'], drop_first=True)
        test_data = pd.concat([test_data, status], axis=1)
        test_data.drop(['building_type'], axis=1, inplace=True)

        pd.set_option('display.max_columns', None)

        self.test_data_new = test_data[['num_rooms', 'area', 'num_bathrooms',
                'ceiling_height', 'newly repaired', 'zero condition', 'Arabkir', 'Center', 'Davtashen',
                'Norq Marash', 'Qanaqer-Zeytun',
                'other', 'panel', 'stone']].copy()

        pred_price = self.reg.predict(self.test_data_new)
        test_data_new = self.test_data_new.assign(Predicted_PRICE=list(pred_price))
        self.pred_price = pred_price
        self.test_data_new = test_data_new.reset_index()
        return self.test_data_new

    def save_db(self):
        db = Regression.myclient["houses"]
        table_info = db["data_house"]
        for i in self.X_test.to_dict('records'):
            existing_document = table_info.find_one(i)
            if not existing_document:
                table_info.insert_one(i)
        return table_info

    def rmse(self):
        RMSE = np.sqrt(mean_squared_error(self.y_test, self.pred_price))
        return f'RMSE: {RMSE}'

    def OLS(self):
        self.X_train = sm.add_constant(self.X_train)  # Adding a constant column to our dataframe
        lm_1 = sm.OLS(self.y_train, self.X_train).fit()
        return lm_1.summary()

    def plott(self):
        # Actual vs Predicted
        c = [i for i in range(1, 1501, 1)]
        fig = plt.figure()
        plt.plot(c, self.y_test, color="blue", linewidth=1, linestyle="-")
        plt.plot(c, self.pred_price, color="green", linewidth=1, linestyle="-")
        fig.suptitle('Actual and Predicted', fontsize=20)
        plt.xlabel('Count', fontsize=18)
        plt.ylabel('Housing Price', fontsize=16)
        plt.show()


if __name__ == '__main__':
    obj = Regression()
    print(obj.preprocessing())
    print(obj.fit())
    print(obj.predict())
    print(obj.save_db())
    print(obj.rmse())
    print(obj.OLS())
    print(obj.plott())
    print(obj.test_preprocessing())