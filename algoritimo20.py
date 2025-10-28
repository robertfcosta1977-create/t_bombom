

import streamlit as st
mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
st.write(mercado)

mercado.sort(key=str.casefold)
st.write(mercado)