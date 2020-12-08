
#The code to a KNN Model can be divided these easy steps

# Step 1 - Load Data
import pandas as pd
dataset = pd.read_csv("https://raw.githubusercontent.com/omairaasim/machine_learning/master/project_11_k_nearest_neighbor/iphone_purchase_records.csv")
print(dataset.head())

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values

# Step - Convert Gender to number (Case based)
from sklearn.preprocessing import LabelEncoder
labelEncoder_gender =  LabelEncoder()
X[:,0] = labelEncoder_gender.fit_transform(X[:,0])

# Step 2 - Split into training and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Step 3 - Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Step 4 - Fit KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, metric="euclidean",p=2)
classifier.fit(X_train, y_train)

# Step 5 - Make Prediction
y_pred = classifier.predict(X_test)

# Step 6 - Evaluating the model
from sklearn import metrics
accuracy = accuracy_score(y_test, y_pred)*100
#confusioin matrix
print(confusion_matrix(y_test, y_pred))
precision = metrics.precision_score(y_test, y_pred) 
print("Precision score:",precision)
#Accuracy of model
print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')
