def Classifier_Tree():
    from sklearn.datasets import load_iris
    from sklearn.utils import shuffle
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import metrics
    iris=load_iris() # call the class
    # print(iris)
    x=iris['data']
    y=iris['target']
    # print(x)
    # print(y)
    x,y=shuffle(x,y,random_state=0) # random shuffle
    # print(x)
    # print(y)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
    # print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
    classifier=DecisionTreeClassifier()
    classifier.fit(x_train,y_train)
    predictions=classifier.predict(x_test)
    # print(predictions)
    # print(y_test)
    # print("Decision Tree classifier model accuracy(in %):", metrics.accuracy_score(y_test,predictions)*100)
    abc=metrics.accuracy_score(y_test,predictions)*100
    return(abc)
a=Classifier_Tree()

### Decision Tree making with graph projection to represent and analyse the results on each node ###

from sklearn.datasets import load_iris # import dataset
from sklearn.utils import shuffle # for suffle the data
from sklearn.model_selection import train_test_split # to split the data into train and test case
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn import tree
import pydot
from sklearn import metrics
import pandas as pd
import numpy as np
iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                     columns=iris['feature_names'] + ['target'])
# df['label'] = df.target.replace(dict(enumerate(df.target_names)))
print(df.head()) # to check the top results
print(iris.feature_names)
print(iris.target_names)
print(df.describe()) # to check difference between min and maxmium value
x = iris['data']
y = iris['target']

iris_df = pd.DataFrame(x, columns=iris['feature_names'])
print(iris_df.head)
x, y = shuffle(x, y, random_state=0)  # random shuffle
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
classifier=DecisionTreeClassifier(criterion="entropy", max_depth=3) # To check accuracy ,applied algorithm
clf = classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) # accuracy result shoecase in console
dot_data = StringIO()
tree.export_graphviz(classifier,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False,
                     proportion=True)
graph=pydot.graph_from_dot_data(dot_data.getvalue()) # plotting the graph
graph[0].write_pdf("iris3.pdf") # run the file.

