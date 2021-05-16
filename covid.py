import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from xgboost.sklearn import XGBClassifier
import xgboost as xgb

def icu(train):
    df = pd.read_excel(train)
    df_new = df.groupby('PATIENT_VISIT_IDENTIFIER', as_index=False)\
    .fillna(method='ffill')\
    .fillna(method='bfill')
#added as PATIENT_VISIT_IDENTIFIER removed during grouping  
    df_new['PATIENT_VISIT_IDENTIFIER'] = df.PATIENT_VISIT_IDENTIFIER
    
    j = 0
    for i in df_new.columns:
        if type(df_new[i].iloc[j]) == str:
            factor = pd.factorize(df_new[i])
            df_new[i] = factor[0]
            definitions = factor[1]
            j = j + 1
            
    
    y = df_new["ICU"]
    X = df_new.drop(['ICU'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, stratify=y)
    xgb1 = XGBClassifier(learning_rate =0.1,
 n_estimators=1000,
 max_depth=5,
 min_child_weight=1,
 gamma=0,eval_metric='mlogloss',
 subsample=0.8,
 colsample_bytree=0.8,
 
 nthread=4,
 scale_pos_weight=1,
 seed=27, use_label_encoder=False )
    xgb1.fit(X_train, y_train)
    preds = xgb1.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    prediction = pd.DataFrame(preds, columns=['predictions']).to_csv('prediction.csv')



    
        

print("Enter the path of the file")
s = input()
icu(s)