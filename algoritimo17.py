# usa uma função 'count()' pra ver quantas vezes a palavra "dolar" apareceu
import streamlit as st

mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
mercado.append('dolar')
st.write(mercado)
st.write("A quantidade de vezes q a palavra dolar aparece é"(mercado.count('dolar')))
