import pandas as pd 
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.model_selection import train_test_split,cross_validate
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score


data = pd.read_csv("formatted_data.csv")

X = data[["Packet_Count","Total_Length","Average_Packet_Interval","Maximum_Packet_Interval","Minimum_Packet_Interval","Average_Packet_Length","Maximum_Packet_Length","Minimum_Packet_Length","Most_Common_Packet_Length"]]
y = data['Label'].map({'youtube': 0, 'reddit': 1,'github': 2, 'honda': 3, 'wikipedia': 4,'bestbuy': 5})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


#split data using train_test_split
    
def model_train(model):
    
    scores = cross_validate(model, X = X_train, y = y_train,cv = 4, scoring = ["f1_macro","accuracy"],return_estimator=True)
    print('Best F1 Score: ',max(scores['test_f1_macro']),'\nBest Accuracy: ',max(scores['test_accuracy']))
    print('Average F1 Score: ',scores['test_f1_macro'].mean(),'\nAverage Accuracy: ',scores['test_accuracy'].mean())
    print(scores['test_f1_macro'],'\n',scores['test_accuracy'])

    df = pd.DataFrame(columns=['f1_macro','accuracy'])


    for model in scores['estimator']:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)
        f1_macro = f1_score(y_test,y_pred,average = 'macro')
        df = pd.concat([df,pd.DataFrame(data = {'f1_macro':[f1_macro],'accuracy':[accuracy]})])

    
    print('Max Prediction Macro F1: ',df.f1_macro.max(),'\nMax Prediction Accuracy: ',df.accuracy.max())
    print('Mean Prediction Macro F1: ',df.f1_macro.mean(),'\nMean Prediction Accuracy: ',df.accuracy.mean())



modelGBC = GradientBoostingClassifier()
modelRidge = RidgeClassifier()

model_train(modelGBC)
model_train(modelRidge)

