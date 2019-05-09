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

