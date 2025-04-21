import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

#import csv as 2d array

data = pd.read_csv("test.csv")

X = data[["packet_count","total_length","ave_packet_int","max_packet_int","min_packet_int","ave_packet_len","max_packet_len","min_packet_length","highest_freq_len"]]
y = data['label'].map({'youtube': 0, 'reddit': 1,'github': 2, 'weather': 3})
#split data using train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#random_state essentially acts as a seed for set reproducability
#print(X_train,"\n",X_test,"\n",y_train,"\n",y_test)
#feed 
modelGBC = GradientBoostingClassifier()
modelGBC.fit(X_train,y_train)

y_pred = modelGBC.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

def model_train(model):
    return