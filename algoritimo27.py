
import streamlit as st
# criar uma lista 'ibov'
ibov = ['bbs3','petra4','adsumus','vale2','ggbr5']

# o elemento do indice 2 ao indice 3
st.write(ibov[2:4])

# o elemnto do indice 1 até o ultimo
st.write(ibov[1:])

# do elemento inicial ao elemento 2
st.write(ibov[:3])

# do elemento inicial até o ultimo saltando de 2 em 2
st.write(ibov[0:5:2])

# selecionar os tres ultimos da lista

st.write(ibov[-3:])

# Selecionar os 2 primeiros elementos da lista
st.write(ibov[:-3])


