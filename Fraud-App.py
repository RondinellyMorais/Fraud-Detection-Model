# Import libraries
import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report



st.set_page_config(layout='wide')


st.write("""
# Detecção de Fraude de transações bancárias ** 
""")

st.sidebar.header('Detecção de Fraude de Cartão')



# Collects user input features into dataframe

def user_input_features():
    
    step = st.sidebar.slider('Step', 0, 750, 200)
    type = st.sidebar.selectbox('Payment Type', ('CASH_OUT', 'PAYMENT', 'TRANSFER', 'CASH_IN', 'DEBIT'))
    amount= st.sidebar.slider('Amount', 0, 10000, 5000)
    oldbalanceOrg = st.sidebar.slider('oldbalanceOrg', 0, 60000, 20000)
    newbalanceOrig = st.sidebar.slider('newbalanceOrig', 0, 50000, 20000)
    oldbalanceDest = st.sidebar.slider('oldbalanceDest', 0, 237000, 100000)
    newbalanceDest = st.sidebar.slider('newbalanceDest', 0, 237000, 100000)
    data = {'step':step,
                'type': type,
                'amount':1000*amount,
                'oldbalanceOrg': 1000*oldbalanceOrg,
                'newbalanceOrig': 1000*newbalanceOrig,
                'oldbalanceDest': 1000*oldbalanceDest,
                'newbalanceDest': 1000*newbalanceDest}
    features = pd.DataFrame(data, index=[0])
    return features

df0 = user_input_features()

dat = pd.read_csv('Fraud-Small.csv')

st.subheader('Exibindo dataset')   
st.dataframe(dat,  height = 400)

st.subheader('Exibindo as features selecionadas')
st.dataframe(df0)

X = dat.drop(['isFraud'], axis=1)
y = dat.isFraud

X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.7, random_state=1234)

categorical_features_indices = np.where(X.dtypes != np.float)[0]
clf = CatBoostClassifier(iterations=500,
                             learning_rate=0.02,
                             depth=12,
                             eval_metric='AUC',
                             random_seed = 42,
                             bagging_temperature = 0.2,
                             od_type='Iter',
                             metric_period = 20,
                             od_wait=25)

clf.fit(X_train, y_train,cat_features=categorical_features_indices,eval_set=(X_validation, y_validation),plot=True)

preds = clf.predict(X_validation)

st.subheader('Valores preditos para os dados de teste')
st.write(preds)

p  = clf.predict(df0)


st.subheader('Resultados da predição do modelo')

fraude = np.array(['Sem fraude: 0','Fraude: 1'])
st.write(fraude[p])


st.write('Confiabilidade do')
st.write(f"ROC-AUC score: {roc_auc_score(y_validation.values, preds)}")