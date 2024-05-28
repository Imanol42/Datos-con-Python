import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
#from sklearn.model_selection import train_test_split

test_patch = 'test.csv'
train_patch = 'train.csv'

#funcion para la carga de archivos
def carga_archivos(ruta):
    return pd.read_csv(ruta)

#cargamos y leemos los datos de testeo
test = carga_archivos('test.csv')
test_copy = test
#cargamos y leemos los datos de entrenamiento
train = carga_archivos('train.csv')
train_copy = train

#definimos la funcion data para poder ver la descripcion de los data-frames
def info_data(data):
    print(data.head())
    print(data.info())
    print(data.describe())
#Tratamos la variable edad para rellenar valores faltantes con la media
def nulos_edad(df): 
    df_re = df.fillna(
        {
            "Age": df["Age"].mean()
        }
    )
    return df_re
#tratamos la variable Sex para asignar valor booleano a los sexos femenino = 0 y masculino = 1 
def genero(sexo):
    df_re = sexo.replace(
        {
            "Sex" : {"male":1 , "female":0}
        }
    )
    return df_re
#tratamos la variables categoricas para convertirlas en valores booleanos
def categorica(data):
    df = data['Embarked']
    df = pd.get_dummies(df, columns=["Embarked"])
    return df
#funcion para redondear valor flotante a valor 1 y 0
def redondear(num):
    return 1 if num >= 0.5 else 0

#datos de entrenamiento
train_copy = nulos_edad(train_copy)
train_copy = genero(train_copy)
df = categorica(train_copy)
df_filtrado_train = pd.concat([train_copy, df], axis=1)

#datos de prueba
test_copy1 = nulos_edad(test_copy)
test_copy2 = genero(test_copy1)
df1 = categorica(test_copy1)
df_filtrado_test = pd.concat([test_copy2, df1], axis=1)

parametros = ['Pclass','Sex','Age','SibSp','Parch','Fare','C','Q','S']
xt = df_filtrado_train[parametros]
yt = df_filtrado_train["Survived"]

#train_x,test_x,train_y,test_y = train_test_split(xt,yt,random_state=1)
#mae = mean_absolute_error(maquina,val_y)
#print(mae)

ML = DecisionTreeRegressor(max_leaf_nodes=10, random_state=1)
ML.fit(xt,yt)

xte = df_filtrado_test[parametros]
df_predict = ML.predict(xte)

#test para ver la presicion del modelo ML
#mae = mean_absolute_error(maquina,val_y)
#print(mae)

df_predict = pd.DataFrame(df_predict)
df_predict['Survived'] = df_predict[0].apply(redondear)

#concatenamos para posterior guardado de archivo csv
df_predict = pd.concat([test['PassengerId'],df_predict['Survived']], axis=1)

#guardamos archivo csv
#df_predict.to_csv('Submission.csv',index=False)

pathsubmi = pd.DataFrame(pd.read_csv('Submission.csv'))
print(pathsubmi)