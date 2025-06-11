# %%
import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from yellowbrick.classifier import ConfusionMatrix

# %%
with open('credit.pkl', 'rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

# %%
X_credit_treinamento.shape

# %%
X_credit_teste.shape

# %%
credit_svm = SVC(kernel='rbf', random_state=1, C= 2.0)
credit_svm.fit(X_credit_treinamento, y_credit_treinamento)


# %%
previsoes = credit_svm.predict(X_credit_teste)
previsoes

# %%
y_credit_teste

# %%
accuracy_score(y_credit_teste, previsoes)

# %%
cm_credit = ConfusionMatrix(credit_svm)
cm_credit.fit(X_credit_treinamento, y_credit_treinamento)
cm_credit.score(X_credit_teste, y_credit_teste)

# %%
print(classification_report(y_credit_teste, previsoes))

# %%
with open('census.pkl', 'rb') as f:
    X_census_treinamento, y_census_treinamento, X_census_teste, y_census_teste = pickle.load(f)

# %%
X_census_treinamento.shape

# %%
X_census_teste.shape

# %%
census_svm = SVC(kernel='linear', random_state=1, C = 1.0)
census_svm.fit(X_census_treinamento, y_census_treinamento)

# %%
previsoes = census_svm.predict(X_census_teste)
previsoes

# %%
y_census_teste

# %%
accuracy_score(y_census_teste, previsoes)

# %%
cm_census = ConfusionMatrix(census_svm)
cm_census.fit(X_census_treinamento, y_census_treinamento)
cm_census.score(X_census_teste, y_census_teste)

# %%
print(classification_report(y_census_teste, previsoes))


