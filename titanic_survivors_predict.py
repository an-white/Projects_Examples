import pandas as pd
import numpy as np

def importacion():
    global df_train, df_test,df_comparar
    train='.\\Preprocesamiento\\Dataset\\train.csv'
    test='.\\Preprocesamiento\\Dataset\\test.csv'
    test_y='.\\Preprocesamiento\\Dataset\\gender_submission.csv'
    # chequear columna faltante
    df_train = pd.read_csv(train)
    df_test =  pd.read_csv(test)
    df_comparar= pd.read_csv(test_y)

def renombrar():
    importacion()
    cabecera=['ID','Sobreviviente','Clase','Nombre','Sexo','Edad','Hermanos','hijos','ticket','tarifa','cabina','Embarque']
    df_train.columns=cabecera
    cabecera=['ID','Clase','Nombre','Sexo','Edad','Hermanos','hijos','ticket','tarifa','cabina','Embarque']
    df_test.columns=cabecera
    cabecera=['ID','Sobreviviente']
    df_comparar.columns=cabecera
    return df_train,df_test,df_comparar

def preprocesamiento():
    global df_test,df_train
    # Transformacion a datos binarios de Sexo
    df_train.Sexo=df_train.Sexo.replace({'male':1,'female':0})
    df_test.Sexo=df_test.Sexo.replace({'male':1,'female':0})

    # Calculo de edad media para edades faltantes
    p=df_train['Edad'].mean()
    p=round(p,0)

    # reemplazo de edad media en edades faltantes
    df_train.Edad=df_train.Edad.replace(np.nan,p)
    df_test.Edad=df_train.Edad.replace(np.nan,p)
    
    # rangos de agrupacion de edades
    bins=[0,5,12,18,35,60,100]
    # nombres de rangos de agrupacion
    names=[1,2,3,4,5,6] 
    df_train.Edad=pd.cut(df_train.Edad,bins,labels=names)
    df_test.Edad=pd.cut(df_test.Edad,bins,labels=names)

    #Eliminacion de nombres para poder utilizar las clases de los pasajeros
    df_train=df_train.drop(['Nombre'],axis=1)
    df_test=df_test.drop(['Nombre'],axis=1)

    # preprocesamiento de tipo de embarque
    df_train.Embarque=df_train.Embarque.replace({'S':0,'C':1,'Q':2})
    df_test.Embarque=df_test.Embarque.replace({'S':0,'C':1,'Q':2})
    return df_train,df_test

def check_stats():
    global y_test,y_p

    from sklearn.metrics import precision_score as ps, accuracy_score as acs, recall_score as rs, f1_score, roc_auc_score
    
    precision= ps(y_test,y_p) # se aplican a los datos de prueba
    print('\nPrecision del modelo:\n',precision)

    exactitud=acs(y_test,y_p) # se aplican a los datos de prueba
    print('\nExactitud del modelo:\n',exactitud)

    re_call=rs(y_test,y_p) # se aplican a los datos de prueba
    print('\nSensibilidad del modelo:\n',re_call)

    F1=f1_score(y_test,y_p) # se aplican a los datos de prueba
    print('\nPuntaje F1 del modelo:\n',F1)

    roc=roc_auc_score(y_test,y_p) # se aplican a los datos de prueba
    print('\nCurva ROC-AUC del modelo:\n',roc)

def bosque(x_train,x_test,y_train):
    global y_p
    print('RFC')
    from sklearn.ensemble import RandomForestClassifier 
    RFC=RandomForestClassifier(n_estimators=500,max_depth=6,criterion='entropy',max_features='sqrt')

    RFC.fit(x_train,y_train)

    y_p=RFC.predict(x_test)
    return y_p

def reg_log(x_train,x_test,y_train):
    global y_p
    print('Regresion Logistica')
    from sklearn.preprocessing import StandardScaler
    SS= StandardScaler()
    x_train= SS.fit_transform(x_train)
    x_test=SS.fit_transform(x_test)

    from sklearn.linear_model import LogisticRegression
    LR=LogisticRegression()

    LR.fit(x_train,y_train)

    y_p=LR.predict(x_test)

renombrar()
preprocesamiento()

from sklearn.linear_model import LinearRegression

# separacion de variables conocidas de entrenamiento y practica
x_train=df_train.iloc[:,2:7] # se define el intervalo de la col inicial hasta la ultima menos 1 que queremos tomar
y_train=df_train.Sobreviviente[:]

x_test=df_test.iloc[:,1:6]
y_test=df_comparar.iloc[:,1]

#reg_log(x_train,x_test,y_train)
bosque(x_train,x_test,y_train)

df=pd.DataFrame(y_p)
df.to_excel('.\\Preprocesamiento\\Prediccion.xlsx')
# chequeo de metricas en el modelo
import metrics
metrics.confusion(y_test,y_p)
metrics.check_stats(y_test,y_p)