## substituir o elemento 'opção' na lista
import streamlit as st

mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
mercado[1] = 'Prata'
st.write(mercado)
