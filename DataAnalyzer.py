import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
x = iris.data
y = iris.target
f = iris.feature_names
df = pd.DataFrame(x,columns=f)

class MlAnalyser:

    def createModel(self):
        knn  = KNeighborsClassifier(n_neighbors=6)
        knn.fit(iris['data'],iris['target'])
        pickle.dump(model, open('KNN_6.pkl', 'wb'))
        return "Ml model of "+str(type(knn))+" is created."

    def predict(self):
        model = pickle.load(open('KNN_6.pkl','rb'))
        prediction = model.predict([exp])
        output = prediction[0]
        return output.item()
        
        

