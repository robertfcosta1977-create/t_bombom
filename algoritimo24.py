# A função "insert" para inserir elemento na lista em uma posição escolhida

import streamlit as st
mercado = ['açóes', 'opções','futuro','dolar','ouro','criptomoedas']
st.write(mercado)
mercado.insert(3,'Prata')
st.write(mercado)


