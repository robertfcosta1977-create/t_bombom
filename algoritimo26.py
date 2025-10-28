# sistema de barbearia
import streamlit as st
st.write("Sistema da Barbearia")
cliente = []

st.write("Gerenciamento da Barbearia")
st.write("1. Cadastrar cliente")
st.write("2. Agendar horário")
st.write("3. Visualizar Agendamento")
st.write("4. Atualizar Agendamento")
st.write("5. Cancelar Agendamento")
st.write("6. sair")

opcao = st.number_input("Digite a opção:")

st.text_input("Digite seu nome:") 
st.date_input("Selecione um data:")
st.time_input("Selecione um horario:")










