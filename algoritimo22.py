# usando a função 'remove',retirar um item da lista

import streamlit as st
mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
mercado.remove('ouro')
st.write(mercado)
