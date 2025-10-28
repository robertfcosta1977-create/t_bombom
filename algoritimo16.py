# Alterar as duas primeiras palavras
import streamlit as st

mercado =['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
mercado[0:2]= ['tesouro','titulo']
st.write(mercado)

