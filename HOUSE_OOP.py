import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from pymongo import MongoClient
from house_price import save


class Regression:
    myclient = MongoClient('localhost', 27017)
    data = pd.read_csv("houses_train.csv")


    def cleaning(self):

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
        X = self.df[['max_floor', 'num_rooms', 'area', 'num_bathrooms',
                'floor', 'ceiling_height', 'newly repaired', 'zero condition', 'Arabkir', 'Avan', 'Center', 'Davtashen',
                'Erebuni', 'Malatia-Sebastia', 'Nor Norq', 'Norq Marash', 'Nubarashen', 'Qanaqer-Zeytun', 'Shengavit',
                'Vahagni district', 'other', 'panel', 'stone']]

        y = self.df['price']  # Target variable

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

        # Create Regression
        # Create Regression
        reg = LinearRegression().fit(X, y)

        # Train Decision Tree Classifer
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
        X_test = self.X_test.assign(Predicted_PRICE=list(pred_price)).reset_index()
        self.pred_price = pred_price
        return pred_price


    def save_db(self):
        db = Regression.myclient["houses"]
        table_info = db["data_house"]
        return save()
#
#        for i in self.X_test.to_dict('records'):
#            existing_document = table_info.find_one(i)
#            if not existing_document:
#                table_info.insert_one(i)
#        return table_info


    def rmse(self):
        RMSE = np.sqrt(mean_squared_error(self.y_test, self.pred_price))
        return RMSE


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


obj = Regression()
print(obj.cleaning())
print(obj.fit())
print(obj.predict())
print(obj.save_db())
print(obj.rmse())
print(obj.plott())