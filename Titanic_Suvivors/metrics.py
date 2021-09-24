def check_stats(y_test,y_p):
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

def confusion(y_test,y_p):
    from sklearn.metrics import confusion_matrix
    matriz=confusion_matrix(y_test,y_p)
    print('\nMatriz de confusion:\n',matriz)
    
if __name__=='__main__':
    #confusion(y_test,y_p)
    #check_stats(y_test,y_p)
    pass