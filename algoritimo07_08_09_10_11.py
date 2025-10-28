# mostrar o conteudo de uma lista e mostrar a primeira posição

import streamlit as st

lista = (10,2,2,4,4,5,6,9,8,8,8,9,5)

# mostrar a lista
st.write(lista)
#mostrar o valor do primeiro da lista
st.write("O primeiro elemento da lista tem o valor de", lista[0])
# mostrar o valor da posição 2 da lista
st.write("O segundo elemento da lista tem valor de",lista[1])
# mostrar o ultimo elemento da lista
st.write("O ultimo elemento da lista é", lista[-1])
#mostrar a quantidade de elementos da lista
st.write("A quantidade de elemento da lista é",len(lista))









