
import streamlit as st

mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
# listar os nomes q contem em mercado
st.write(mercado)
# mostrar os 3 primeiros elementos 
st.write(mercado[0:3])
# verificar se uma palavra consta na lista
fut = 'dolar' in mercado
st.write(fut)





