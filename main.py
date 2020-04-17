#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.info()


# In[4]:


black_friday[black_friday.Gender=='F'].groupby("Age").count()['User_ID']


# In[5]:


print( black_friday.User_ID.count(), black_friday.User_ID.nunique())


# In[6]:


((black_friday.Product_Category_2.isnull().sum())+(black_friday.Product_Category_3.isnull().sum()))/(12*537577 )


# In[7]:


print(black_friday.Product_Category_2.isnull().sum())
print(black_friday.Product_Category_3.isnull().sum())


# In[8]:


black_friday.Product_Category_3.describe()


# In[9]:


black_friday.Product_Category_3.mode()


# In[10]:


black_friday.Product_Category_3.value_counts()


# In[11]:


df_normalizaPurchase=black_friday[~black_friday.Purchase.isnull()]


# In[12]:


df_normalizaPurchase.head()


# In[13]:


print(black_friday.Purchase.min())
print(black_friday.Purchase.max())

def normalizarPurchase(Purchase):
    return ((Purchase - 185)/(23961-185))


# In[15]:


black_friday['PurchaseNormalizada']=black_friday['Purchase'].apply(normalizarPurchase)


# In[16]:


black_friday.PurchaseNormalizada.describe()


# In[17]:


black_friday.PurchaseNormalizada.mean()


# In[18]:


black_friday['Purchase'].describe()


# In[34]:


media=df_normalizaPurchase['Purchase'].mean()
desvio=df_normalizaPurchase['Purchase'].std()

def padronizaPurchase(Purchase):
      return (Purchase-media)/desvio


# In[35]:


black_friday['PurchasePadronizada']=black_friday['Purchase'].apply(padronizaPurchase)


# In[57]:


len(black_friday['PurchasePadronizada'].loc[ (black_friday['PurchasePadronizada']<=1) &(black_friday['PurchasePadronizada']>-1) ])


# In[59]:


df_aux=black_friday[['Product_Category_2','Product_Category_3']]


# In[61]:


df_aux[df_aux.Product_Category_2.isnull()].describe()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return 537577,12
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return 49348
    


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return 5891
    


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return 3
    


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return 0.08375311815795691
    


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return 373299
    


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return 16
    


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return 0.384794
    


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    return 348631
    


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True
    

