import pandas as pd
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.model_selection import train_test_split, TunedModelClassifierCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, make_scorer

#import csv as 2d array

data = pd.read_csv("formatted_data.csv")

X = data[["Packet_Count","Total_Length","Average_Packet_Interval","Maximum_Packet_Interval","Minimum_Packet_Interval","Average_Packet_Length","Maximum_Packet_Length","Minimum_Packet_Length","Most_Common_Packet_Length"]]
y = data['Label'].map({'youtube': 0, 'reddit': 1,'github': 2, 'weather': 3, 'wikipedia': 4,'bestbuy': 5})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#split data using train_test_split
    
def model_train(model):
    

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    print('Classification Report:')
    print(classification_report(y_test, y_pred))

def model_tuning():
    return

modelGBC = GradientBoostingClassifier()
modelLogisticReg = LogisticRegression()
modelRidge = RidgeClassifier()

model_train(modelGBC)
#model_train(modelLogisticReg)
#model_train(modelRidge)

