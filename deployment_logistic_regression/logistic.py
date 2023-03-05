# pip install pandas
import pandas as pd
import numpy as np
# pip install matplotlib
import matplotlib.pyplot as plt
# pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the CSV
dataset = pd.read_csv('DR.csv')
# print(dataset.head());
#
# Graph
# plt.scatter(dataset.temperature, dataset.res)
# plt.show()

# Convert strings to numeric
dataset.type = dataset.type.replace(to_replace=['no', 'yes'], value=[0, 1])
dataset.Gender = dataset.Gender.replace(to_replace=['no', 'yes'], value=[0, 1])
dataset.beginner = dataset.beginner.replace(to_replace=['no', 'yes'], value=[0, 1])
dataset.res = dataset.res.replace(to_replace=['safe', 'not'], value=[0, 1])

# Create the Logistic Regression Model
model = LogisticRegression(max_iter=500)
model.fit(dataset[['speed', 'type', 'Gender', 'beginner', 'passenger']], dataset.res)
# Save the model
with open('logistic.pk', 'wb') as f:
	pickle.dump(model, f)

# Test the model
test_speed = 45
test_type = 'yes'
test_Gender = 'no'
test_beginner = 'yes'
test_type = 1 if test_type == 'yes' else 0
test_Gender = 1 if test_Gender == 'yes' else 0
test_beginner = 1 if test_beginner == 'yes' else 0
test_passenger = 1


output = model.predict_proba([[test_speed, test_type, test_Gender, test_beginner, test_passenger]])
print("Safe", "{:.2f}".format(output[0][0]))
print("Not", "{:.2f}".format(output[0][1]))

X = dataset[['speed','type','Gender','beginner', 'passenger']]
Y = dataset['res']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
X_train.describe()
X_test.describe()
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
		                     metric_params=None, n_jobs=None, n_neighbors=5, p=2,
		                     weights='uniform')
knn.score(X_test, y_test)
print("Accuracy for K=5 : ",  "{:.4f}".format(knn.score(X_test, y_test)))

##K=6
knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
print("Accuracy for K=6 : ",  "{:.4f}".format(knn.score(X_test, y_test)))


##K=7
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
print("Accuracy for K=7 : ",  "{:.4f}".format(knn.score(X_test, y_test)))


##K=8
knn = KNeighborsClassifier(n_neighbors = 8)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
print("Accuracy for K=8 : ",  "{:.4f}".format(knn.score(X_test, y_test)))

##K=9
knn = KNeighborsClassifier(n_neighbors = 9)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
print("Accuracy for K=9 : ",  "{:.4f}".format(knn.score(X_test, y_test)))

knn = KNeighborsClassifier(n_neighbors = 10)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
print("Accuracy for K=10 : ",  "{:.4f}".format(knn.score(X_test, y_test)))
