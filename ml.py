import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from matplotlib import pyplot as plt
import pandas as pd 
from sklearn.linear_model import RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,cross_validate
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score


data = pd.read_csv("formatted_data.csv")

X = data[["Packet_Count","Total_Length","Average_Packet_Interval","Maximum_Packet_Interval","Minimum_Packet_Interval","Average_Packet_Length","Maximum_Packet_Length","Minimum_Packet_Length","Most_Common_Packet_Length"]]
y = data['Label'].map({'youtube': 0, 'reddit': 1,'honda': 2, 'wikipedia': 3,'bestbuy': 4})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


#split data using train_test_split
    
def model_train(model,name):
    
    print('\n'+name+' Stats:'+'\n')
    scores = cross_validate(model, X = X_train, y = y_train,cv = 4, scoring = ["f1_macro","accuracy"],return_estimator=True)
    print('Best F1 Score: ',max(scores['test_f1_macro']),'\nBest Accuracy: ',max(scores['test_accuracy']))
    print('Average F1 Score: ',scores['test_f1_macro'].mean(),'\nAverage Accuracy: ',scores['test_accuracy'].mean())
    print('Individual F1 Scores:\n',scores['test_f1_macro'],'\n','Individual Accuracy Scores:\n',scores['test_accuracy'],'\n')

    df = pd.DataFrame(columns=['f1_macro','accuracy'])


    for model in scores['estimator']:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)
        f1_macro = f1_score(y_test,y_pred,average = 'macro')
        df = pd.concat([df,pd.DataFrame(data = {'f1_macro':[f1_macro],'accuracy':[accuracy]})])

    print('Predictions Evaluation Metrics')
    print('Max Prediction Macro F1: ',df.f1_macro.max(),'\nMax Prediction Accuracy: ',df.accuracy.max())
    print('Mean Prediction Macro F1: ',df.f1_macro.mean(),'\nMean Prediction Accuracy: ',df.accuracy.mean())

    ConfusionMatrixDisplay.from_predictions(y_test,y_pred,display_labels=['Youtube','Reddit','Honda','Wikipedia','BestBuy'])
    plt.title(name+' Confusion Matrix')
    plt.show()
    



modelGBC = GradientBoostingClassifier()
modelRidge = RidgeClassifier()
modelKNN = KNeighborsClassifier()

model_train(modelGBC,'Gradient Boosting Classifier')
model_train(modelRidge,'Ridge Classifier')
model_train(modelKNN,'K Neighbors Classifier')
