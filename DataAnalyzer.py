from io import StringIO
from DataStore import BlobDataReader
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt


class MlModel:

    dataReader = BlobDataReader()
    knn  = KNeighborsClassifier(n_neighbors=6)

    def getData(self):
        data = self.dataReader.readData()
        return data

    def createModel(self):
        dataSet = self.dataReader.readData()
        data = pd.read_csv(StringIO(dataSet))
        X = data.iloc[:,:-1].values
        y = data.iloc[:, -1].values
        x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=123)
        self.knn.fit(x_train,y_train)
        y_test_pred = self.knn.predict(x_test)
        accuracy = accuracy_score(y_test, y_test_pred)*100

        return "Ml model of "+str(type(self.knn))+" is created."

    def predict(self):
        #model = pickle.load(open('KNN_6.pkl','rb'))
        prediction = model.predict([exp])
        output = prediction[0]
        return output.item()
        
        

