## REQUERIMENTS
import pandas as pd
from sklearn import linear_model
import streamlit as sl
###

##DF
df=pd.read_csv("machinel/teste.csv")
df.plot(kind="scatter", x="X",y="Y");
modelo=linear_model.LinearRegression()
x=df[["X"]]
y=df[["Y"]]
modelo.fit( x, y)
##

##WEB
sl.title("GRAFICO LINEAR F(x)")
sl.divider()
##

#CODE
# print("Hello World")
num=sl.number_input("Digite o X e retornará o Y: ")
if num:
    ipsilon=modelo.predict([[num]])[0][0]
    sl.write(f"O valor de Y com X de: {num:.2f} é igual a: {ipsilon:.2f}")
##