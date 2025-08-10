import json
import re
from itertools import combinations
import streamlit as st
import streamlit.components.v1 as components
from connection import iniciar, dados_base
from EndPoints_Structure_Tables import post_new_info, extrair_inf_sys, buscar_tabelas_por_coluna

components.html(
    """
    <div style="
        border: 2px solid #4CAF50; 
        background-color: #e8f5e9; 
        padding: 15px; 
        border-radius: 8px; 
        text-align: center;
        font-family: Arial, sans-serif;
        color: #2e7d32;
        margin-bottom: 20px;">
        <strong>Anúncio</strong><br>
        Conheça o melhor chatbot do mercado!<br>
        <a href="http://localhost:8501/" target="_blank" 
        style="color:#1b5e20; text-decoration: underline;">
        Saiba mais aqui
      </a>
    </div>
    """,
    height=100,
)

iniciar_objs = iniciar()
# Initialization
if 'colecao' not in st.session_state:
    st.session_state['colecao'] = iniciar_objs[2]


if __name__ == "__main__":
    st.set_page_config( page_title="ChatBot", icon=":heavy_plus_sign:")
    st.title("Chatbot")
    entrada = st.text_input("Digite o que deseja saber:", "")
    extrair_inf_sys(entrada,"1",st.session_state.colecao)
    buscar_tabelas_por_coluna(entrada, st.session_state.colecao)
    post_new_info(entrada,st.session_state.colecao)
