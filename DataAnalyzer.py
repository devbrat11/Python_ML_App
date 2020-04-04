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

knn  = KNeighborsClassifier(n_neighbors=6)
knn.fit(iris['data'],iris['target'])
print(knn)
        

