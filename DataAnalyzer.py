import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
##For logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

class TestAnalyzer:

    def predict(self,heartrate,noise):
        data=pd.read_csv("HearCareHealthData.csv")
        inputColumns=data.loc[:,['HeartRate', 'Noise']]
        outputColumn=data.loc[:,['Target']]
        x_train,x_test,y_train,y_test=train_test_split(inputColumns,outputColumn,test_size=0.2,random_state=123)
        model=LogisticRegression()
        model.fit(x_train,y_train)

        exp=[heartrate,noise]
        prediction = model.predict([exp])
        output = prediction[0]
        return output.item()

    def Analysis(self):
        return "Analysis VAlue"  