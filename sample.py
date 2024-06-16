import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report

data=pd.read_csv('Iris.csv')
print(data.head())

missing=data.isnull().sum()
print(missing)

if 'Id' in data.columns:
    data.drop('Id',axis=1,inplace=True)
    print(data.head())

label=LabelEncoder()
data['Species']=label.fit_transform(data['Species'])
print(data.head())

a=data.drop('Species',axis=1)
b=data['Species']

a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=.2,random_state=50)

svm_classifier=SVC(kernel='linear',random_state=50)

svm_classifier.fit(a_train,b_train)
b_pred=svm_classifier.predict(a_test)

acc=accuracy_score(b_test,b_pred)
print(f'{acc:.2f}')

print(classification_report(b_test,b_pred))