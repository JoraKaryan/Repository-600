import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from pymongo import MongoClient


myclient = MongoClient('localhost', 27017)


df = pd.read_csv("houses_train.csv")
df=df.set_index('Unnamed: 0')

for i in df['price']:
       if not isinstance(i,int):
              raise TypeError('The type of variables must be integers')

fill_ceiling_height = round(df.loc[:,"ceiling_height"].mean())
df[['ceiling_height']]=df[['ceiling_height']].fillna(fill_ceiling_height)

fill_floor = round(df.loc[:,"floor"].mean())
df[['floor']]=df[['floor']].fillna(fill_floor)

fill_num_bathrooms = round(df.loc[:,"num_bathrooms"].mean())
df[['num_bathrooms']]=df[['num_bathrooms']].fillna(fill_num_bathrooms)
fill_area = round(df.loc[:,"area"].mean())
df[['area']]=df[['area']].fillna(fill_area)
fill_num_rooms = round(df.loc[:,"num_rooms"].mean())
df[['num_rooms']]=df[['num_rooms']].fillna(fill_num_rooms)
fill_max_floor = round(df.loc[:,"max_floor"].mean())
df[['max_floor']]=df[['max_floor']].fillna(fill_max_floor)
fill_price = round(df.loc[:,"price"].mean())
df[['price']]=df[['price']].fillna(fill_price)





#1 condition-expand
status = pd.get_dummies(df['condition'],drop_first=True)
df = pd.concat([df,status],axis=1)
df.drop(['condition'],axis=1,inplace=True)
#2 district-expand
status = pd.get_dummies(df['district'],drop_first=True)
df = pd.concat([df,status],axis=1)
df.drop(['district'],axis=1,inplace=True)
#3 building_type-expand
status = pd.get_dummies(df['building_type'],drop_first=True)
df = pd.concat([df,status],axis=1)
df.drop(['building_type'],axis=1,inplace=True)

pd.set_option('display.max_columns', None)


#split dataset in features and target variable

X = df[['max_floor', 'num_rooms', 'area', 'num_bathrooms',
       'floor', 'ceiling_height', 'newly repaired', 'zero condition', 'Arabkir', 'Avan', 'Center', 'Davtashen', 'Erebuni', 'Malatia-Sebastia', 'Nor Norq', 'Norq Marash', 'Nubarashen', 'Qanaqer-Zeytun', 'Shengavit', 'Vahagni district', 'other', 'panel', 'stone']]

y = df['price'] # Target variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test





# Create Regression
reg = LinearRegression().fit(X,y)

# Train Decision Tree Classifer
reg = reg.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = reg.predict(X_test)
reg.score(X,y)

#X_train = sm.add_constant(X_train)    # Adding a constant column to our dataframe
#lm_1 = sm.OLS(y_train,X_train).fit()
#print(lm_1.summary())




pred_price = reg.predict(X_test)
X_test = X_test.assign(Predicted_PRICE = list(pred_price))


#RMSE = np.sqrt(mean_squared_error(y_test, pred_price))
X_test = X_test.reset_index()
X_test = X_test.to_dict('records')


db = myclient["houses"]
table_info = db["data_house"]

def save():
       for i in X_test:
              existing_document = table_info.find_one(i)
              if not existing_document:
                     table_info.insert_one(i)
       return table_info










