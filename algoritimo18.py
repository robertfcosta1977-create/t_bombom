# acrescentar elementos na lista

import streamlit as st

mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
mercado.extend(['petrobras','BB','CEF'])
st.write(mercado)

